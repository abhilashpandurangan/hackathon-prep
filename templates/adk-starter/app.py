"""Simple Streamlit chat UI for the ADK starter agent."""

import asyncio

import streamlit as st
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agent import root_agent

APP_NAME = "adk_starter"


@st.cache_resource
def get_runner():
    session_service = InMemorySessionService()
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)
    return runner, session_service


async def _new_session_id(session_service) -> str:
    session = await session_service.create_session(app_name=APP_NAME, user_id="user")
    return session.id


async def _ask(runner, session_id: str, text: str) -> str:
    content = types.Content(role="user", parts=[types.Part(text=text)])
    events = runner.run_async(user_id="user", session_id=session_id, new_message=content)
    replies = []
    async for event in events:
        if event.is_final_response() and event.content and event.content.parts:
            replies.append(event.content.parts[0].text)
    return "\n".join(replies) or "(no response)"


def ask(text: str) -> str:
    runner, session_service = get_runner()
    if "session_id" not in st.session_state:
        st.session_state.session_id = asyncio.run(_new_session_id(session_service))
    return asyncio.run(_ask(runner, st.session_state.session_id, text))


st.title("ADK Starter Agent")
st.caption("Google ADK + Streamlit. Add tools in agent.py where marked.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = ask(prompt)
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})

if st.sidebar.button("Reset conversation"):
    st.session_state.pop("session_id", None)
    st.session_state.messages = []
    st.rerun()
