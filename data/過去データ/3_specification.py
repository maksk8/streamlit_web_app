import streamlit as st

st.title('csv変換アプリ')
st.caption('2025/11/18')
st.subheader('仕様書')

with open("data/仕様書.txt", "r", encoding="utf-8") as f:
    text = f.read()

st.text(text)
