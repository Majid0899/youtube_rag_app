from fastapi import APIRouter
from backend.schemas.request_schema import QueryRequest
from backend.services.youtube_service import YoutubeRAGService

router = APIRouter()
rag_service = YoutubeRAGService()

@router.post("/ask")
async def ask_video(request: QueryRequest):

    answer = rag_service.query_video(
        request.youtube_url,
        request.query
    )

    return {"answer": answer}
