import streamlit as st

st.title("🤖 Meu Robô")
nome = st.text_input("Qual é o seu nome?")
if st.button("Falar com o robô"):
    st.success(f"Olá, {nome}! Estou funcionando!")
