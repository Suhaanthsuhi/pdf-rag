class IngestionService:
    def __init__(self, pdf_loader, vector_store):
        self.pdf_loader = pdf_loader
        self.vector_store = vector_store

    def ingest(self, pdf_path: str):
        document = self.vector_store.get_document_by_filename(pdf_path)

        if document:
            print("Document already indexed.")
            return document

        chunks = self.pdf_loader.load(pdf_path)

        document = self.vector_store.insert_document(pdf_path)

        self.vector_store.insert_chunks(
            document_id=document.uid,
            chunks=chunks,
        )

        return document
