import streamlit as st
import requests

st.set_page_config(page_title="QueryGenie", page_icon="🧞")
st.title("🧞 QueryGenie — Ask your database anything")

API_URL = "https://querygenieapi.onrender.com"

question = st.text_input("Apna sawaal likho:", placeholder="e.g. total revenue by region")

if st.button("Generate & Run") and question:
    with st.spinner("Sochte hue..."):
        resp = requests.post(f"{API_URL}/query", json={"question": question})
    if resp.status_code == 200:
        data = resp.json()
        st.code(data["sql"], language="sql")
        st.dataframe(data["rows"])
    else:
        st.error(resp.json().get("detail", "Kuch galat ho gaya"))