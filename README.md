# 📄 Personalised PDF QA Bot

An AI-powered Question Answering system that allows users to upload PDF documents and ask questions about their content.
The system retrieves relevant information from the document and generates accurate answers using a local Large Language Model (LLM).

This project demonstrates how **Retrieval-Augmented Generation (RAG)** can be used to build an intelligent document assistant.

---

# 🚀 Features

* Ask questions from PDF documents
* Local AI inference (no cloud required)
* Retrieval-Augmented Generation (RAG)
* Semantic search for relevant document chunks
* Fast and efficient response generation
* Simple Python-based implementation

---

# 🧠 Technologies Used

* Python
* LangChain
* FAISS Vector Database
* Local LLM (Mistral 7B)
* Sentence Transformers
* PDF processing libraries

---

# 📂 Project Structure

```
personalised_QA_Bot
│
├── app.py                # Main application script
├── requirements.txt      # Python dependencies
├── research.pdf          # Sample PDF document
├── document.pdf          # Sample PDF document
├── zydus.pdf             # Sample PDF document
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/Abhimanyu1Shukla/personalised_QA_Bot.git
```

### 2️⃣ Navigate to the project folder

```
cd personalised_QA_Bot
```

### 3️⃣ Install required dependencies

```
pip install -r requirements.txt
```

---

# 📥 Download the AI Model

This project uses a **local LLM model**.

GitHub does not allow uploading large model files (>100MB), so the model must be downloaded separately.

Download the model from:

Mistral 7B GGUF model

Example file:

```
mistral-7b-instruct-v0.1.Q4_K_M.gguf
```

After downloading, place the model file inside the project folder.

---

# ▶️ Run the Application

Run the following command:

```
python app.py
```

The program will load the PDF documents, create embeddings, and allow you to ask questions related to the document content.

---

# 🧠 How It Works

The system follows a **Retrieval-Augmented Generation (RAG)** pipeline:

1. PDF documents are loaded
2. Text is split into smaller chunks
3. Embeddings are created using sentence transformers
4. FAISS vector database stores document embeddings
5. User query is converted into embeddings
6. Relevant document chunks are retrieved
7. The LLM generates the final answer

---

# 💡 Future Improvements

* Web interface for easier interaction
* Support for multiple PDF uploads
* Faster embedding models
* Document summarization
* Cloud deployment

---

# 👨‍💻 Author

**Abhimanyu Shukla**
Computer Science Student

---

# ⭐ Contribution

Contributions, suggestions, and improvements are welcome.

If you find this project helpful, please consider giving it a ⭐ on GitHub.
