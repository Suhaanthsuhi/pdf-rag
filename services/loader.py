from typing import Any
from pypdf import PdfReader


class PdfLoader:
    def __init__(self, chunk_size: int = 500):
        self.chunk_size = chunk_size

    def load(self, path: str) -> list[dict[str, Any]]:
        reader = PdfReader(path)
        documents = []

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""

            if not text.strip():
                continue

            chunks = [
                text[i : i + self.chunk_size]
                for i in range(0, len(text), self.chunk_size)
            ]

            for chunk_index, chunk in enumerate(chunks):
                documents.append(
                    {
                        "page": page_number,
                        "chunk_index": chunk_index,
                        "content": chunk,
                        "source": path,
                    }
                )

        return documents
    

__all__ = [
    "PdfLoader"
]