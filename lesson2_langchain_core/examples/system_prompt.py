from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
llm=ChatOpenAI()

systemPrompt=ChatPromptTemplate.from_messages([
    ("system","you are a cricket expert and please return the answer in JSON format"),
    ("human","could you tell who hold Highest run in an ODI {game}")
])

chain=systemPrompt|llm
res=chain.invoke({"game":"cricket"})
print(res.content)
