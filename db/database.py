from sqlalchemy import create_engine
from .models import Base

DATABASE_URL = 'postgresql+psycopg://suhaanthvv:postgres@localhost:5432/pdf_rag'
engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    print("Checking and creating tables if they do not exist...")
    
    # This safely runs "CREATE TABLE IF NOT EXISTS" for all your registered models
    Base.metadata.create_all(engine)
    
    print("Database initialization complete!")

if __name__ == "__main__":
    init_db()