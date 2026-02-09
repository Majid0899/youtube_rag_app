import streamlit as st
import httpx
import asyncio

BACKEND_URL = "http://localhost:8000/ask"

st.title("🎥 YouTube RAG Chatbot")

youtube_url = st.text_input("Enter YouTube URL")
query = st.text_input("Ask Question")

async def fetch_answer(payload):
    async with httpx.AsyncClient() as client:
        response = await client.post(BACKEND_URL, json=payload)
        return response.json()

if st.button("Ask"):

    payload = {
        "youtube_url": youtube_url,
        "query": query
    }

    result = asyncio.run(fetch_answer(payload))

    st.success(result["answer"])
