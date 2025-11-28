from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI()
inner_prompt = PromptTemplate.from_template("Explain {concept}")
outer_prompt = PromptTemplate.from_template("As a teacher:\n\n{explanation}")

formatted_inner = inner_prompt.format(concept="LLMs")
final = outer_prompt.format(explanation=formatted_inner)

print(final)