from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

from backend.services.vector_service import VectorService
from backend.services.llm_service import LLMService

class RAGService:

    def __init__(self):
        self.vector_service = VectorService()
        self.llm_service = LLMService()

    def build_rag_chain(self, transcript):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150
        )

        docs = splitter.split_text(transcript)

        vector_db = self.vector_service.create_vector_store(docs)

        retriever = vector_db.as_retriever()

        llm = self.llm_service.get_llm()

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever
        )

        return qa_chain
