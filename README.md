# LangChain Tutorial

This is a simple Python project that shows how to build a PDF question answering app with LangChain.

The app reads a PDF file, breaks the text into small chunks, turns those chunks into embeddings, stores them in a Postgres database, and then answers a question using the most relevant chunks from the PDF.

## What This Project Does

1. Loads a PDF from `data/pdfs/`.
2. Splits the PDF text into small pieces.
3. Creates embeddings with `sentence-transformers/all-MiniLM-L6-v2`.
4. Saves the PDF chunks and embeddings in Postgres using pgvector.
5. Searches for the chunks most related to a question.
6. Sends those chunks to a Groq chat model through LangChain.
7. Prints the answer in the terminal.

## Project Structure

```text
main.py                  Main file that runs the full app
services/loader.py       Loads and splits PDF text
services/embedding.py    Creates embeddings
services/vector_store.py Saves and searches chunks in Postgres
services/ingestion.py    Adds a PDF to the database
services/rag.py          Runs the question answering flow
services/llm.py          Creates the chat model
prompts/prompt.py        Prompt used for answering questions
db/database.py           Database connection
db/models.py             Database tables
data/pdfs/               PDF files used by the app
```

## Requirements

- Python 3.13 or newer
- Postgres
- pgvector extension
- Groq API key
- uv

## Setup

Install the Python packages:

```bash
uv sync
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Create a Postgres database named `pdf_rag`.

This project currently connects to Postgres with this URL:

```text
postgresql+psycopg://suhaanthvv:postgres@localhost:5432/pdf_rag
```

You can change it in `db/database.py` if your Postgres username, password, host, or database name is different.

Inside the database, enable the needed extensions:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

## Run

Run the project with:

```bash
uv run python main.py
```

The app will:

1. Create the database tables if they do not exist.
2. Load `data/pdfs/EJ1172284.pdf`.
3. Store the PDF chunks if the PDF is not already indexed.
4. Ask this question:

```text
What is this pdf about? who is its author?
```

5. Print the answer.

## How To Change The Question

Open `main.py` and change this line:

```python
question = 'What is this pdf about? who is its author?'
```

Replace it with your own question.

## How To Use Another PDF

Put your PDF file inside `data/pdfs/`.

Then update this line in `main.py`:

```python
ingestion.ingest("data/pdfs/EJ1172284.pdf")
```

Change it to your PDF path.

## Simple Explanation

This project is a basic RAG app.

RAG means the app does not answer only from the model's memory. It first looks inside your PDF, finds the most useful text, and gives that text to the model. Then the model answers using that text.

The prompt tells the model to answer only from the PDF context. If the answer is not in the PDF text, it should say:

```text
I don't know.
```
