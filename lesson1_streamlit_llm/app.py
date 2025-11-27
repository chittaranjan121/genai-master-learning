import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

st.title("🧠 My First LLM Chat App")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar settings
with st.sidebar:
    st.header("⚙️ Settings")
    model_choice = st.selectbox(
        "Choose a model",
        ["groq/llama-3.1-8b-instant", "openai/gpt-4o-mini"]
    )
    clear_chat = st.button("🗑️ Clear Chat")

# Clear chat button
if clear_chat:
    st.session_state.messages = []
    st.rerun()

# LLM function
def get_llm_response(prompt):
    if model_choice.startswith("groq"):
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Chat input
user_input = st.text_input("💬 Ask anything:")

if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        ai_reply = get_llm_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

# Display chat history
st.write("---")
st.subheader("Chat History")

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 AI:** {msg['content']}")
