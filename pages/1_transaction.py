import streamlit as st
import pandas as pd

# st.write(st.__version__)

st.title('csv変換アプリ')
st.caption('2025/11/18')
st.subheader('今月の取引履歴')
# st.text('テキスト')

if 'df_1s' in st.session_state:
    df_1ss = st.session_state['df_1s']
    html = df_1ss.to_html(index=False)
    st.markdown(html, unsafe_allow_html=True)
