import os 
import chainlit as cl 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

template = """Question: {question}
Answer: Let's think step by step"""

@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(
        template=template, input_variables=["question"])
    llm_chain = LLMChain(
        prompt = prompt,
        llm = OpenAI(temperature = 0),
        verbose = True)
    return llm_chain