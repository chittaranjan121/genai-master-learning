from langchain_classic.memory import ConversationBufferMemory, ConversationSummaryMemory, ConversationEntityMemory
from langchain_classic import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)
memory = ConversationBufferMemory()

prompt = PromptTemplate.from_template("""
You are a helpful assistant.
Chat history:
{history}
User: {input}
""")

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

print(chain.run("Hi, my name is Chittaranjan"))
print(chain.run("What is my name?"))
