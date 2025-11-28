from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()
llm=ChatOpenAI()

template="""
classify the emotion

Example1: 
Input:I got a Promotion!
Emotion:Joy

Example2:
Input: I lost my wallet
Emotion: Sad

Example 3:
Input: Someone is chasing me!
Emotion: Fear

Now classify:
Input: {text}
Emotion:
"""
prompt=PromptTemplate(
    template=template
)
chain=prompt|llm
res=chain.invoke({"text":"I coud not get my dog"})
print(res.content)