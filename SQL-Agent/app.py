from dotenv import load_dotenv
import streamlit as st 
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent

load_dotenv()

st.set_page_config(page_title="Talk to your Database")
st.header("Talk to your database")

db = SQLDatabase.from_uri("sqlite:///my_demo.db")

llm = ChatOpenAI(temperature=0)

agent_executor = create_sql_agent(
    llm, db = db, agent_type = "openai-tools", verbose = True
)

user_question = st.text_input("Ask a question about your database:")

if user_question is not None and user_question != "":
    with st.spinner(text="In progress..."):
        response = agent_executor.invoke(user_question)
        st.write(response["output"])


