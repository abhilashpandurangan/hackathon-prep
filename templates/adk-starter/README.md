# ADK Starter

A minimal Google Agent Development Kit agent with a Streamlit chat UI.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # then put your key in .env
```

## Run

```bash
streamlit run app.py
```

## What you need

- A Google API key with Gemini access. Set `GOOGLE_API_KEY` in `.env`.
  Get one at https://aistudio.google.com/apikey

## Customize

- `agent.py`: add tools where marked `ADD YOUR TOOLS HERE`, change the
  model where marked `MODEL`.
- `app.py`: the chat loop is the tested core. Add new UI as extra Streamlit
  panels instead of rewriting it.
