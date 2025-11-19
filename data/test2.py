import pandas as pd
import sys
import os
input_file = sys.argv[1]
#input_file = '売上データ_2025年11月.csv'
df_1 = pd.read_csv(input_file)

df_2 = pd.read_csv(r'C:\Users\f\project_pandas_01\顧客コード.csv')
pd_3 = pd.merge(df_1, df_2, on='company_name', how='left')

pd_4 = pd_3.loc[:, ['ticker_code', 'sales_amount']]

output_path = os.path.join(os.path.dirname(input_file), 'result.csv')
pd_4.to_csv(output_path, encoding='utf-8-sig', index=False)
print(f"出力完了: {output_path}")
input("Enterキーで終了します。")