from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm=ChatOpenAI()
parser=JsonOutputParser()
prompt=PromptTemplate(
    template="Extract JSON from this text:\n{text}\n\n{format_instructions}",
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | llm | parser
print(chain.invoke({"text": "John is 20 years old."}))