from datetime import datetime
from sqlalchemy import String, Text, func, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from pgvector.sqlalchemy import Vector

class Base(DeclarativeBase):
    pass

class Document(Base):
    __tablename__ = 'documents'

    uid: Mapped[str] = mapped_column(
        String(36),
        primary_key=True, 
        server_default=func.gen_random_uuid().cast(String)
    )
    filename: Mapped[str] = mapped_column(String(250))
    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now()
    )

    # Optional: Back-reference to access chunks easily from a document object
    # e.g., my_doc.chunks
    chunks: Mapped[list["DocumentChunk"]] = relationship(
        back_populates="document", 
        cascade="all, delete-orphan"
    )

class DocumentChunk(Base):
    __tablename__ = 'document_chunks'

    uid: Mapped[str] = mapped_column(
        String(36),
        primary_key=True, 
        server_default=func.gen_random_uuid().cast(String)
    )
    
    # Explicitly links chunks to the documents table with automatic deletion cleanup
    document_id: Mapped[str] = mapped_column(
        ForeignKey("documents.uid", ondelete="CASCADE"),
        index=True
    )
    
    chunk_index: Mapped[int]
    page_number: Mapped[int]
    content: Mapped[str] = mapped_column(Text)
    
    # FIXED: Type hint changed to list[float] so your IDE and SQLAlchemy understand it
    embedding: Mapped[list[float]] = mapped_column(Vector(384))

    # Optional: Pair relationship helper
    document: Mapped["Document"] = relationship(back_populates="chunks")
