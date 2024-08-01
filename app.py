from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os

# function to load OpenAI model and get response
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.6)
    response = llm.invoke(question)
    return response

# initialize streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input: ", key=input)
response = get_openai_response(input)

submit = st.button("Generate Response")

if submit:
    st.subheader("The response is")
    st.write(response)