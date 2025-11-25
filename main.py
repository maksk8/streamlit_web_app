import streamlit as st
import pandas as pd

# st.write(st.__version__)
st.title('csv変換アプリ')
# st.caption('2025/11/18')
# st.subheader('subheader')
# st.text('テキスト')

tab1, tab2 = st.tabs(["処理", "仕様書"])

with tab1:

    # 複数ファイルの選択を許可しない
    uploaded_file = st.file_uploader("csvファイル選択", type='csv', accept_multiple_files=False)

    if uploaded_file is not None:
        df_1 = pd.read_csv(uploaded_file)
        df_2 = pd.read_csv('./data/顧客コード.csv')
        df_3 = pd.merge(df_1, df_2, on='company_name', how='left')
        df_4 = df_3.loc[:, ['date', 'ticker_code', 'sales_amount']]
        
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
    with open("data/仕様書.txt", "r", encoding="utf-8") as f:
        text = f.read()
    st.code(text)

    st.subheader('例：処理前データ')
    example_a = pd.read_csv('./data/売上データ_2025年11月.csv')
    st.dataframe(
        example_a, 
        column_config={
            "transaction_id": st.column_config.TextColumn("No."),
            "date": st.column_config.TextColumn("取引日"), 
            "company_name": st.column_config.TextColumn("会社名"), 
            "sales_amount": st.column_config.TextColumn("売上金額"), 
        },
        hide_index=True,
        height=150
    )

    st.subheader('例：顧客データ')
    example_b = pd.read_csv('./data/顧客コード.csv')
    st.dataframe(
        example_b, 
        column_config={
            "number": st.column_config.TextColumn("No."),
            "company_name": st.column_config.TextColumn("会社名"), 
            "ticker_code": st.column_config.TextColumn("顧客コード"), 
            "sector": st.column_config.TextColumn("業種"), 
        },
        hide_index=True,
        height=150
    )

    st.subheader('例：処理後データ')
    example_c = pd.read_csv('./data/result.csv')
    st.dataframe(
        example_c, 
        column_config={
            "date": st.column_config.TextColumn("取引日"),
            "ticker_code": st.column_config.TextColumn("顧客コード"), 
            "sales_amount": st.column_config.TextColumn("売上金額"), 
        },
        hide_index=True,
        height=150
    )
