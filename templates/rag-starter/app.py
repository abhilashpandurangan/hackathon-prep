"""Simple Streamlit UI for RAG: add documents, ask questions.

Storage is a local ChromaDB vector store (./chroma_db). Embeddings run
locally, no key needed. Answer generation uses OpenAI when OPENAI_API_KEY is
set, otherwise it returns the retrieved chunks verbatim.
"""

import os

import chromadb
import streamlit as st

CHROMA_PATH = "./chroma_db"
COLLECTION = "docs"


@st.cache_resource
def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    return client.get_or_create_collection(COLLECTION)


def chunk_text(text: str, size: int = 500) -> list[str]:
    """Naive chunker. UPGRADE THIS FIRST when quality matters: split on
    sentences or paragraphs instead of fixed character windows."""
    return [text[i : i + size] for i in range(0, len(text), size) if text[i : i + size].strip()]


def add_document(name: str, text: str) -> int:
    collection = get_collection()
    chunks = chunk_text(text)
    existing = collection.count()
    collection.add(
        ids=[f"{name}-{existing + i}" for i in range(len(chunks))],
        documents=chunks,
        metadatas=[{"source": name} for _ in chunks],
    )
    return len(chunks)


def retrieve(query: str, n: int = 4) -> list[str]:
    collection = get_collection()
    results = collection.query(query_texts=[query], n_results=n)
    return results["documents"][0] if results["documents"] else []


def answer_with_llm(query: str, docs: list[str]) -> str:
    from openai import OpenAI

    client = OpenAI()
    context = "\n\n".join(docs)
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer using only the context below. "
                    "If the answer is not in the context, say so plainly."
                ),
            },
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"},
        ],
    )
    return resp.choices[0].message.content


def answer_fallback(docs: list[str]) -> str:
    return (
        "No OPENAI_API_KEY set, so here are the retrieved chunks verbatim:\n\n"
        + "\n\n---\n\n".join(docs)
    )


st.title("RAG Starter")
st.caption("Local ChromaDB + Streamlit. Paste docs, ask questions.")

with st.expander("Add a document", expanded=get_collection().count() == 0):
    doc_name = st.text_input("Document name", value="notes.txt")
    doc_text = st.text_area("Document text", height=200)
    if st.button("Add document") and doc_text.strip():
        n = add_document(doc_name or "doc", doc_text)
        st.success(f"Added {n} chunks from {doc_name}.")

st.divider()

query = st.text_input("Ask a question about your documents")
if query:
    docs = retrieve(query)
    if not docs:
        st.warning("No documents yet. Add one above first.")
    else:
        with st.spinner("Thinking..."):
            if os.getenv("OPENAI_API_KEY"):
                st.markdown(answer_with_llm(query, docs))
            else:
                st.markdown(answer_fallback(docs))
        with st.expander("Retrieved chunks"):
            for d in docs:
                st.markdown(d)
                st.markdown("---")

st.sidebar.write(f"Chunks in store: {get_collection().count()}")
if st.sidebar.button("Clear all documents"):
    coll = get_collection()
    ids = coll.get()["ids"]
    if ids:
        coll.delete(ids=ids)
    st.rerun()
