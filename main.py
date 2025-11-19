import streamlit as st
import pandas as pd

# st.write(st.__version__)

st.title('csv変換アプリ')
st.caption('2025/11/18')
# st.subheader('subheader')
# st.text('テキスト')

# 複数ファイルの選択を許可しない
uploaded_file = st.file_uploader("csvファイル選択", type='csv', accept_multiple_files=False)

if uploaded_file is not None:
    df_1 = pd.read_csv(uploaded_file)
    st.session_state['df_1s'] = df_1
    df_2 = pd.read_csv('./data/顧客コード.csv')
    df_3 = pd.merge(df_1, df_2, on='company_name', how='left')
    df_4 = df_3.loc[:, ['ticker_code', 'sales_amount']]
    
    result = df_4.to_csv(index=False).encode('utf-8')

    st.download_button(
        label='変換csvダウンロード',
        data=result,
        file_name="result.csv",
        mime="text/csv"
    )

    st.dataframe(df_4, hide_index=True)

# with st.form(key='profile_form'):
#     name = st.text_input('名前')
#     submit_btn = st.form_submit_button('送信')
#     if submit_btn:
#         st.text(f'登録:{name}')
