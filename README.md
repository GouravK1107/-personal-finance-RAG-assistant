# 📊 Personal Finance RAG Assistant

A Retrieval-Augmented Generation (RAG) based AI assistant that answers personal finance questions using content extracted from PDF documents.

This project combines:

- Local embeddings using Sentence Transformers  
- FAISS for vector similarity search  
- Google Gemini for answer generation  
- Streamlit for the frontend interface  

---

## 🚀 What This Project Does

1. Reads multiple PDF files from the `documents/` folder  
2. Extracts and chunks text  
3. Generates semantic embeddings locally  
4. Stores embeddings in a FAISS vector database  
5. Retrieves relevant context based on user queries  
6. Uses Gemini to generate grounded answers  

The system ensures responses are based only on the uploaded financial documents.

---

## 🏗 Architecture Overview
PDF Documents
↓
Text Extraction (pypdf)
↓
Chunking
↓
Local Embeddings (SentenceTransformer)
↓
FAISS Vector Database
↓
Similarity Search
↓
Gemini (Answer Generation)
↓
Streamlit Frontend


---

## 🛠 Tech Stack

- Python
- Sentence Transformers (`all-MiniLM-L6-v2`)
- FAISS (Vector Search)
- Google Gemini API
- Streamlit
- PyPDF

---

### 4️⃣ Run the Application after cloning

streamlit run app.py

The app will open in your browser.

---

## 💡 Example Questions

- What is budgeting?
- How does compound interest work?
- What are different investment options?
- What is an emergency fund?
- How does retirement planning work?

---

## 🔒 Why Local Embeddings?

Initially, embeddings were generated using the Gemini API.  
However, API rate limits caused quota issues when processing large PDFs.

To solve this:

- Embeddings are generated locally using Sentence Transformers
- Gemini is used only for answer generation
- No embedding API limits
- Faster performance
- Scalable architecture

---

## 📈 Future Improvements

- Add file upload feature in UI  
- Add metadata (file name + page number in answers)  
- Persist FAISS index to disk  
- Deploy to Streamlit Cloud  
- Add evaluation metrics  

---

## 🎯 Project Goal

This project demonstrates how to build a production-style RAG pipeline using:

- Open-source embeddings
- Efficient vector search
- LLM-based answer generation
- Interactive web interface

It serves as a portfolio-level implementation of modern AI system design.

---

## 👨‍💻 Author

Gourav K  
BCA Student | Backend & AI Enthusiast  
Focused on mastering Computer Vision & AI systems.

---

⭐ If you found this project useful, consider starring the repository!
