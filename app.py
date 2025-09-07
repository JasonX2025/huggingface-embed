from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

class TextRequest(BaseModel):
    text: str

@app.post("/embed")
def embed_text(request: TextRequest):
    vector = model.encode(request.text).tolist()
    return {"vector": vector}