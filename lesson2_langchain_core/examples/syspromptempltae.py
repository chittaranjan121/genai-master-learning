from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI Assistant."),
    
    # Few-shot example
    ("human", "Convert to JSON: Apple is a fruit."),
    ("assistant", '{{"item": "Apple", "category": "fruit"}}'),
    
    # Actual user message
    ("human", "{query}")
])

# Create chain
chain = prompt | llm

# Invoke
res = chain.invoke({"query": "who is india's best wicket keeper in ODI cricket"})

# Print output text
print(res.content)
