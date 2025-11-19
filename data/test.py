import streamlit as st
import pandas as pd
import io

st.title("CSVデータ処理ツール (Streamlit)")

# 1. アップロード
uploaded_file = st.file_uploader("CSVデータを選択してください", type=["csv"])

if uploaded_file is not None:
    # ファイルをPandas DataFrameに変換
    df_uploaded = pd.read_csv(uploaded_file)
    
    st.write("---")
    st.subheader("処理前のデータ")
    st.dataframe(df_uploaded.head()) # データを表示
    
    # -----------------------------------------------
    # 2. 処理ロジック (ここにあなたのマージ処理が入る)
    # -----------------------------------------------
    # 仮の処理として、簡単なフィルタリングを実行
    df_processed = df_uploaded[['顧客コード', '売上']].copy() 
    
    # -----------------------------------------------
    
    st.subheader("処理後のデータ")
    st.dataframe(df_processed.head())
    
    # 3. ダウンロード (処理後のDataFrameをダウンロード可能にする)
    
    # DataFrameをCSV形式のバイト列に変換
    csv_buffer = io.StringIO()
    df_processed.to_csv(csv_buffer, index=False)
    csv_bytes = csv_buffer.getvalue().encode('utf-8')
    
    st.download_button(
        label="✅ 処理結果をダウンロード",
        data=csv_bytes,
        file_name="processed_sales_data.csv",
        mime="text/csv"
    )