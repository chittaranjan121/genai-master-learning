import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

st.set_page_config(page_title="Test")
st.title("TestBot")

# Store chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar - model selection
model_choices = st.sidebar.selectbox(
    "choose a model",
    ["groq/llama-3.1-8b-instant", "openai/gpt-4o-mini"]
)

# Chat window
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
user_input = st.chat_input("Ask something")

def get_llm(prompt):
    if model_choices.startswith("groq"):
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    
    elif model_choices.startswith("openai"):
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

if user_input:
    # show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # get ai response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = get_llm(user_input)
            st.write(answer)

    # save AI reply
    st.session_state.messages.append({"role": "assistant", "content": answer})
