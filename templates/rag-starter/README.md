# RAG Starter

Retrieval-augmented Q&A over your own documents, with a Streamlit UI. Paste
docs in, ask questions, get answers grounded in what you added.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## What you need

- Nothing, to start. The vector store (ChromaDB) and embeddings run locally;
  documents persist in `./chroma_db`.
- For generated answers instead of verbatim chunks, set `OPENAI_API_KEY`
  in your environment.

## Customize

- `app.py`: the first real upgrade is `chunk_text` — split on sentences or
  paragraphs instead of fixed character windows.
- Tune `retrieve()`'s `n` (number of chunks) per question type: more for
  "summarize everything", fewer for precise lookups.
