from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st 

model = OllamaLLM(model="gemma3")

template = """Question : {question}
Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model 

st.title("Chatbot with Ollama")

user_input = st.text_input("Type a question:")

if user_input:
    response = chain.invoke({"question":user_input})
    st.write("Response:", response)



