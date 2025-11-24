import streamlit as st
import pandas as pd

# st.write(st.__version__)
st.title('csv変換アプリ')
# st.caption('2025/11/18')
# st.subheader('subheader')
# st.text('テキスト')

tab1, tab2, tab3, tab4 = st.tabs(
    ["メインタブ", "アップロードデータ確認", "顧客データ確認", "仕様書"]
)

with tab1:

    # 複数ファイルの選択を許可しない
    uploaded_file = st.file_uploader("csvファイル選択", type='csv', accept_multiple_files=False)

    if uploaded_file is not None:
        df_1 = pd.read_csv(uploaded_file)
        df_2 = pd.read_csv('./data/顧客コード.csv')
        df_3 = pd.merge(df_1, df_2, on='company_name', how='left')
        df_4 = df_3.loc[:, ['ticker_code', 'sales_amount']]
        
        result = df_4.to_csv(index=False).encode('utf-8')

        if result is not None:
            st.download_button(
                label='変換csvダウンロード',
                data=result,
                file_name="result.csv",
                mime="text/csv"
            )

        if df_4 is not None:
            html = df_4.to_html(index=False)
            st.subheader('処理結果')
            st.markdown(html, unsafe_allow_html=True)


with tab2:
    if uploaded_file is not None:
        st.dataframe(df_1, hide_index=True)
    else:
        st.write("アップロード前")


with tab3:
    client = pd.read_csv('./data/顧客コード.csv')
    st.dataframe(client, hide_index=True)

with tab4:
    with open("data/仕様書.txt", "r", encoding="utf-8") as f:
        text = f.read()
    st.text(text)
