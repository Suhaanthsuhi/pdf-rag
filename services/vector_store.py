from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from db.models import Document, DocumentChunk

class VectorStoreService:
    def __init__(self, engine, embedding_service):
        self.engine = engine
        self.embedding = embedding_service
    
    def get_document_by_filename(self, filename: str):
        with Session(self.engine) as session:
            return session.scalar(
                select(Document).where(Document.filename == filename)
            )

    def insert_document(self, filename: str) -> Document:
        with Session(self.engine) as session:
            document = Document(filename=filename)
            session.add(document)

            session.commit()
            session.refresh(document)
            return document

    def insert_chunks(self, document_id: str, chunks: List):
        with Session(self.engine) as session:
            texts = [
                c['content']
                for c in chunks
            ]

            vectors = self.embedding.embed_documents(texts)

            rows = [
                DocumentChunk(
                    document_id=document_id,
                    page_number=chunk["page"],
                    chunk_index=chunk["chunk_index"],
                    content=chunk["content"],
                    embedding=vector,
                )
                for chunk, vector in zip(chunks, vectors)
            ]

            session.add_all(rows)
            session.commit()

    def similarity_search(self, query: str, limit: int = 5):
        query_vector = self.embedding.embed_query(query)

        with Session(self.engine) as session:
            statement = (
                select(DocumentChunk)
                .order_by(
                    DocumentChunk.embedding.cosine_distance(query_vector)
                )
                .limit(limit)
            )
            results = session.scalars(statement).all()

            return results
        
__all__ = [
    "VectorStoreService"
]