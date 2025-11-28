from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

prompt=PromptTemplate(
    template="Explain {topic} on cricket",
    input_variables=['topic']
)
prompt.format(topic="Cricket")