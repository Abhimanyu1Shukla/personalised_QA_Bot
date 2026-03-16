from langchain_community.llms import LlamaCpp
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

import os
import time
 
MODEL_PATH = "/Users/abhimanyushukla/Desktop/pdf_qa_bot-main/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
PDF_PATH = "/Users/abhimanyushukla/Desktop/pdf_qa_bot-main/zydus.pdf"
 
llm = LlamaCpp(
    model_path=MODEL_PATH,
    temperature=0.1,      
    max_tokens=256,      
    top_p=0.9,
    n_ctx=1024,          
    n_batch=128,        
    f16_kv=True,
    verbose=False,
    stop=["\n\n", "Question:", "Context:"],  
)
 
print("🔄 Loading PDF...")
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()
 
print("✂️ Splitting text...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
docs = text_splitter.split_documents(documents)
 
print("🧠 Creating embeddings...")
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embedding)
 
print(f"✅ Ready! Processed {len(documents)} pages into {len(docs)} chunks")
print("🤖 Ask questions about the PDF. Type 'exit' to quit.\n")
 
while True:
    query = input("❓ Your question: ")
    if query.lower() == "exit":
        break
 
    try:
        print("🔍 Searching for relevant content...")
        start_time = time.time()
        
        relevant_docs = vectorstore.similarity_search(query, k=2)  
        
        if not relevant_docs:
            print("❌ No relevant content found.")
            continue
        
        pages = [doc.metadata.get('page', 'Unknown') for doc in relevant_docs]
        print(f"📄 Found content from pages: {pages}")
        
        context = "\n\n".join([doc.page_content for doc in relevant_docs])
        context = context[:800]  
        print(f"📏 Context length: {len(context)} characters")
        print(f"📝 Preview: {context[:150]}...")
        
        prompt = f"""Based on the document text below, answer the question.
 
Document text:
{context}
 
Question: {query}
 
Answer (be concise and specific):"""
 
        print(f"🤔 Generating answer (prompt length: {len(prompt)})...")
        
        gen_start = time.time()
        response = llm.invoke(prompt)
        gen_time = time.time() - gen_start
        
        print(f"✅ Generated in {gen_time:.1f} seconds")
        print("\n🤖 Answer:")
        print("-" * 40)
        print(response.strip())
        print("-" * 40)
        print(f"📚 Sources: Pages {pages}\n")
        
    except KeyboardInterrupt:
        print("\n⏹️ Generation interrupted by user")
        continue
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("💡 Try a simpler question or restart the program\n")
 