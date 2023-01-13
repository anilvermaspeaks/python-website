import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
with col2:
    st.title("Anil Verma")
    content ="""
    Hi there 👋, I am Anil Verma I am a passionate Full Stack 
    Web Developer 
    who is fascinated by complex engineering problems.
    """
    st.write(content)

footer_info = """
   Ask me anything about web development.
    """
st.write(footer_info)