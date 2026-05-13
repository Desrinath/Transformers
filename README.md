# 📄 PDF QA AI — Transformer Notes + RAG Project

This repository contains:

- 📘 My Transformer Architecture Notes
- 🤖 PDF QA AI Project
- 🧠 RAG (Retrieval Augmented Generation) Workflow
- ⚙️ Full setup instructions
- 🚀 Local LLM integration using Ollama

This project helps beginners understand how modern AI-powered document question-answering systems work internally.

---

# 📚 Repository Contents

## 1️⃣ Transformer Notes

Inside this repository, I have included my learning notes related to:

- Transformer Architecture
- Encoder & Decoder
- Attention Mechanism
- Self Attention
- Positional Encoding
- Large Language Models (LLMs)
- RAG Systems

These notes can help beginners understand the theory behind modern AI systems.

---

## 2️⃣ PDF QA AI Project

This project allows users to:

✅ Upload PDF documents  
✅ Extract text from PDFs  
✅ Generate embeddings  
✅ Store vectors using FAISS  
✅ Ask questions from uploaded PDFs  
✅ Get AI-generated answers locally using Ollama  

---

# 🧠 Project Workflow

```text
User Upload PDF
        ↓
Extract PDF Text
        ↓
Split Text into Chunks
        ↓
Generate Embeddings
        ↓
Store Embeddings in FAISS
        ↓
User Asks Question
        ↓
Question → Embedding
        ↓
Semantic Similarity Search
        ↓
Retrieve Relevant Chunks
        ↓
Send Context + Question to LLM
        ↓
Generate Final Answer
