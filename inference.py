import pickle
import os
import shutil
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"] = "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"


with open('vector_data.pkl', 'rb') as f:
    db = pickle.load(f)



st.title("classEasy Student Helper")

chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
main_placeholder = st.empty()
query = main_placeholder.text_input("Question: ")

docs = db.similarity_search(query)
result = (chain.run(input_documents=docs, question=query))
st.header("Answer")
st.write(result)