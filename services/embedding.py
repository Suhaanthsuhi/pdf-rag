from langchain_huggingface import HuggingFaceEmbeddings

class EmbeddingService:
    def __init__(self):
        self.model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    
    def embed_query(self, text: str):
        return self.model.embed_query(text)
    
    def embed_documents(self, documents: list[str]):
        return self.model.embed_documents(documents)


__all__ = [
    "EmbeddingService"
]