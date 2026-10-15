"""Simple Streamlit chat UI for the LangGraph starter agent."""

import streamlit as st

from agent import agent

st.title("LangGraph Starter Agent")
st.caption("LangGraph ReAct agent + Streamlit. Add tools in agent.py where marked.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

config = {"configurable": {"thread_id": "starter-thread"}}

if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply_parts = []
            for chunk in agent.stream(
                {"messages": [("user", prompt)]}, config=config, stream_mode="values"
            ):
                last = chunk["messages"][-1]
                if last.type == "ai" and last.content:
                    reply_parts.append(
                        last.content if isinstance(last.content, str) else str(last.content)
                    )
            reply = "\n".join(reply_parts) or "(no response)"
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})

if st.sidebar.button("Reset conversation"):
    st.session_state.messages = []
    st.rerun()
