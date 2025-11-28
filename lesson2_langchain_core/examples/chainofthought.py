from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
llm=ChatOpenAI()

template = """
Solve the problem step-by-step and then give the final answer.

Question: {question}
"""

prompt = PromptTemplate.from_template(template)
chain = prompt | llm
res=chain.invoke({"question": "If 20% of 50 is x, what is x?"})
print(res.content)
