from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI()
prompt=PromptTemplate(
    template="give details about a wicket keeper in game of {sport}",
    input_variables=['sport']
)

chain=prompt|llm
res=chain.invoke({"sport":"cricket"})
print(res.content)