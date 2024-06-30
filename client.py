import streamlit as st
from app import agent_run

st.title('RESEARCH ASSISTANT ')
input_text=st.text_input("Search the topic u want")



if input_text:
    st.write(agent_run(input_text))