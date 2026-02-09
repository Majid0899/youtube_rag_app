# YouTube RAG Chatbot

## Overview
This project is a Full Stack GenAI application that allows users to query YouTube videos using Retrieval Augmented Generation (RAG).

The system extracts transcripts from YouTube videos, creates embeddings, stores them in a vector database, and uses an LLM to generate contextual answers.

---

## Tech Stack

- FastAPI (Async Backend)
- Streamlit (Frontend UI)
- LangChain (Orchestration)
- HuggingFace Inference API (LLM)
- FAISS (Vector Database)

---

## Features

- Query any YouTube video
- Semantic search on transcript
- Async API calls
- Modular architecture
- Production scalable design

---

## Setup

### 1 Install Dependencies
    pip install -r requirements.txt
### 2 Setup Environment Variables
    .env:
        HUGGINGFACE_API_KEY=Your Key
        MODEL_NAME=Model Name
### 3 Run Backend
    uvicorn backend.main:app --reload
### 4 Run Frontend
    streamlit run frontend/app.py