import streamlit as st
from main2 import ask_question  # import your function

st.title("📊 Personal Finance RAG Assistant")

question = st.text_input("Ask a question about personal finance:")

if st.button("Ask !"):
    if question:
        answer = ask_question(question)
        st.write("### Answer:")
        st.write(answer)
