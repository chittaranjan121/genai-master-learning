from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI()
template="""
Title:{title}
Uppercase Title: {title_upper}
"""
prompt=PromptTemplate(
    template=template,
    input_variables=['title'],
    partial_variables={"title_upper":lambda title:title.upper()}
)
chain=prompt|llm
res=chain.invoke({"title":"who is mr kohli"})
print(res.content)