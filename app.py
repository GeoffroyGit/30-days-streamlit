import streamlit as st

st.header("Hello and welcome")

st.write("Welcome to a world of buttons")

if st.button("Say hello"):
    st.write("Well, hello there")
else:
    st.write("Goodbye")
