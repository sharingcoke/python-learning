import adata
import pandas as pd
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
# k_type: k线类型：1.日；2.周；3.月 默认：1 日k
res_df = adata.stock.market.get_market(stock_code='000001', k_type=1, start_date='2023-01-01')
print(res_df)
column_data = res_df['change']
print(column_data)