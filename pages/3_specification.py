import streamlit as st

st.write(st.__version__)

st.title('csv変換アプリ')
st.caption('2025/11/18')
st.subheader('仕様書')
st.text('会社名から会社コードに変換')
st.text('レガシーシステムから今月の売上を抽出し、新システムにデータを挿入')
st.text('注意点')
st.text('1.中間生成ファイルはcsv形式')
st.text('2.レガシーシステムからのcsvは会社名と売上金額のみ')
st.text('3.新システムインポートは顧客コードのみ')
st.text('4.顧客コードのデータベースあり')
