from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()
llm=ChatOpenAI()

template = """
Convert the sentence into sentiment.

Example:
Input: I love pizza.
Output: Positive

Now classify:
Input: {text}
Output:
"""
prompt=PromptTemplate(
    template=template
)
chain=prompt|llm
res=chain.invoke({"text":"I lodon't like Cricket"})
print(res.content)