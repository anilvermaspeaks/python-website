import streamlit as st
import pandas

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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("./data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://github.com/anilvermaspeaks)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://github.com/anilvermaspeaks)")
