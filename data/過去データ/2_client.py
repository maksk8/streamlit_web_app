import streamlit as st
import pandas as pd

# st.write(st.__version__)

st.title('csv変換アプリ')
st.caption('2025/11/18')
st.subheader('顧客コード一覧')
# st.text('テキスト')

df_2 = pd.read_csv('./data/顧客コード.csv')

html = df_2.to_html(index=False)

st.markdown(html, unsafe_allow_html=True)
