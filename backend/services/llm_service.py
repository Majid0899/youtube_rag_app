from langchain_huggingface import HuggingFaceEndpoint
from backend.core.config import settings

class LLMService:

    def get_llm(self):

        return HuggingFaceEndpoint(
            repo_id=settings.MODEL_NAME,
            huggingfacehub_api_token=settings.HF_API_KEY,
            temperature=0.3,
            max_new_tokens=512
        )
