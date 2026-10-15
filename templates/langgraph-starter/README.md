# LangGraph Starter

A minimal LangGraph ReAct agent with conversation memory and a Streamlit
chat UI.

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

- An OpenAI API key. Set `OPENAI_API_KEY` in `.env`. The default model is
  `gpt-4o-mini`; any model string your setup supports works.

## Customize

- `agent.py`: add tools where marked `ADD YOUR TOOLS HERE`, change the
  model where marked `MODEL`.
- `app.py`: the chat loop is the tested core. Add new UI as extra Streamlit
  panels instead of rewriting it.
