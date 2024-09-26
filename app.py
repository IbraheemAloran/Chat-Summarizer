import streamlit as st
from transformers import pipeline

st.title("Chat Summarizer")

model = pipeline("text2text-generation", model="ibraheemaloran/dialogue_bart")

chat = st.text_area("Enter chat log or dialogue")

if st.button("Summarize"):
    summary = model("summarize: \n\n" + chat)
    st.write(summary)
