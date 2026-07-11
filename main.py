import os
from dotenv import load_dotenv
from db.database import init_db, engine

from prompts.prompt import chat_prompt
from services.rag import RagService
from services.embedding import EmbeddingService
from services.loader import PdfLoader
from services.vector_store import VectorStoreService
from services.ingestion import IngestionService
from services.llm import LLM

load_dotenv()

init_db()

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')

embedding = EmbeddingService()

vector_store = VectorStoreService(
    engine=engine,
    embedding_service=embedding,
)

loader = PdfLoader(chunk_size=500)

ingestion = IngestionService(
    pdf_loader=loader,
    vector_store=vector_store,
)

llm = LLM().model()

rag = RagService(
    vector_store=vector_store,
    prompt=chat_prompt,
    llm=llm,
)

ingestion.ingest("data/pdfs/EJ1172284.pdf")

question = 'What is the summary of this pdf?'

response = rag.answer(question)

print("\n", response.content)