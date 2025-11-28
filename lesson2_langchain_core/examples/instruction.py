from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
llm=ChatOpenAI()

prompt=PromptTemplate(template="Summerize the following text in 2 bullet points:\n\n {text}")
chain=prompt|llm
res=chain.invoke({"text":"Snowflake Cortex Search provides semantic search across tables."})
print(res.content)