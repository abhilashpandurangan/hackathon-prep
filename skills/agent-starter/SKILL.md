---
name: agent-starter
description: Generates a minimal working starter for an agentic app: ADK, LangGraph, or RAG, each with a simple chat UI. Use when starting a new agent build or hackathon project.
---

# Agent Starter

Use this skill when the builder wants a starting point for an agentic app.
It generates a minimal, working scaffold: an agent plus a simple UI, ready
to run and extend. It works with any AI agent; adapt the tool names to
whatever your agent provides.

## Pick the template

- Ask which framework fits, or infer it from context. The three templates
  live in `templates/` in this repo:
  - `adk-starter`: Google Agent Development Kit agent with tools, served
    through a Streamlit chat UI. Best when the builder already uses Google
    models or wants ADK's session and tooling model.
  - `langgraph-starter`: LangGraph ReAct agent with tools and conversation
    memory, served through a Streamlit chat UI. Best for explicit control
    over the agent loop.
  - `rag-starter`: retrieval-augmented Q&A over the builder's own documents,
    with a local vector store and a Streamlit UI for adding docs and asking
    questions. Best when the value is "chat with my data".

- If the builder does not know, default to `langgraph-starter` for agent
  behavior or `rag-starter` for document Q&A. Say why you picked it in one
  line.

## Generate the starter

- Copy the whole template folder into the builder's project. Keep every
  file: `agent.py`, `app.py`, `requirements.txt`, `.env.example`, and
  `README.md`.

- Install dependencies from `requirements.txt` and run the app once to
  confirm it works before handing it over. Fix what breaks; do not hand
  over a scaffold you have not run.

- Tell the builder the two commands: how to install and how to run. They are
  in each template's README.

## Customize it

- Add tools where the template marks `ADD YOUR TOOLS HERE`. One tool is a
  plain function with a docstring; the framework picks it up from there.

- Change the model in exactly one place, marked `MODEL` in each template.
  Keep everything else untouched until the new model is confirmed working.

- Extend the UI by adding a new Streamlit panel, not by rewriting `app.py`.
  The chat loop is the tested core; panels are additive.

- For the RAG template, the first real upgrade is a better chunking strategy
  in the marked function, not a bigger model.

## What not to do

- Do not add authentication, databases, or deployment config to a starter.
  Those are day-two concerns and they slow down the first win.

- Do not wire real credentials or production data into the scaffold. Use the
  `.env.example` pattern and sample data until the builder says otherwise.

- Do not mix frameworks in one starter. If the builder outgrows the
  template, scaffold the next one separately and migrate deliberately.
