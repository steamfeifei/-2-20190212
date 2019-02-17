import pandas as pd
import os
# os.chdir(r'C:\Users\Lenovo\PycharmProjects\untitled\dm\data')
data = pd.read_excel('loans.xls')
print(data.head())

# del data['每月归还额']
# print(data.head())
# print(data.贷款期限.value_counts())
# print(data.贷款金额.groupby(by = data.还款状态).mean())
# print(data.贷款金额.describe())
# print(data.贷款金额.mean())
# print(data.贷款金额.std())
# print(data.贷款金额.var())
# print(data.贷款金额.max())
# print(data.贷款金额.min())
# print(data.贷款金额.median())
# print(data.贷款金额.mode())
df = data.sort_values(['发放贷款日期','贷款金额'],ascending=[False,True])
# #df.reset_index(inplace=True)
# #print(df.columns)
# df['每月归还额'] = df['贷款金额']/df.贷款期限
# #print(df.账户号.dtype)
df1 = df[(df.账户号 > 2000) | (df.账户号 < 5000)][['发放贷款日期','贷款金额']]
print(df1)