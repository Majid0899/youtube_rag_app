from backend.utils.transcript_loader import load_transcript
from backend.services.rag_service import RAGService

class YoutubeRAGService:

    def __init__(self):
        self.rag_service = RAGService()

    def query_video(self, url: str, question: str):

        transcript = load_transcript(url)

        rag_chain = self.rag_service.build_rag_chain(transcript)

        response = rag_chain.invoke(question)

        return response["result"]
