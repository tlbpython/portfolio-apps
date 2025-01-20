import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Tracy")
    content = """
    Hello , I am learning more python today """

    st.info(content)


content2 = """Below are soem apps I created """
st.write(content2)