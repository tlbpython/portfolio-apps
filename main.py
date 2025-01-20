import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/taz.png")

with col2:
    st.title("Tracy")
    content = """
    Hello , I am learning more python today """

    st.info(content)