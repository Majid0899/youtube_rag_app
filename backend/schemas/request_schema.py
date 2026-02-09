from pydantic import BaseModel

class QueryRequest(BaseModel):
    youtube_url: str
    query: str
