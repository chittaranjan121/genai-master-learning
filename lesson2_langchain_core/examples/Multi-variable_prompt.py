from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI()
prompt=PromptTemplate(
    template="Translate {sentence} to {language}.",
    input_variables=["sentence","language"]
)
chain=prompt|llm
res=chain.invoke({"sentence":"I LOVE YOU","language":"hindi"})
print(res.content)