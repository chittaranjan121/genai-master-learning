import streamlit as st
from dotenv import load_dotenv
import os
from groq import Groq
load_dotenv()

st.title("My First LLM App")
st.set_page_config(page_title="Learn")

model_choices=st.sidebar.selectbox(
    "choose a model",
    ["groq/llama-3.1-8b-instant", "openai/gpt-4o-mini"]
)
user_input = st.text_input("Ask me anything:")

def get_llm_response(prompt):
    if model_choices.startswith("groq"):
        client=Groq(api_key=os.getenv("GROQ_API_KEY"))
        response=client.chat.completions.create(
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
if st.button("Generate"):
    if user_input:
        with st.spinner("Thinking..."):
            answer = get_llm_response(user_input)
        st.success(answer)    



