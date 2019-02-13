# 1、读入loans数据表，删除列，列名为每月归还额（10分）
# 2、对指定列做频数统计，列名为贷款期限（10分）
# 3、对指定列做分组统计，列名为还款状态。在此基础上，计算各分组贷款金额列的均值（20分）
# 4、统计贷款金额的均值、最小值、最大值、中位数、方差（15分）
# 5、对数据进行排序，按照发放贷款日期（降序）贷款金额（升序）排序（15分）
# 6、按照贷款金额除以贷款期限计算生成新列，并命名为每月归还额（10分）
# 7、提取行（账户号在2000到5000之间）列（发放贷款日期和贷款金额）数据框（20分）

import pandas as pd
import os
os.chdir(r'C:\Users\Lenovo\PycharmProjects\untitled\dm\data')
data = pd.read_excel('loans.xlsx')
print(data.head())

del data['每月归还额']
print(data.head())
print(data['贷款期限'].value_counts())
print(data.贷款金额.groupby(by = data.还款状态).mean())
print(data.贷款金额.describe())
print(data.贷款金额.mean())
print(data.贷款金额.std())
print(data.贷款金额.var())
print(data.贷款金额.max())
print(data.贷款金额.min())
print(data.贷款金额.median())
print(data.贷款金额.mode())
df = (data.sort_values(['发放贷款日期','贷款金额'],ascending=[False,True]))
#df.reset_index(inplace=True)
#print(df.columns)
df['每月归还额'] = df['贷款金额']/df.贷款期限
#print(df.账户号.dtype)
print(df)
df1 = df[(df.账户号 > 2000) & (df.账户号 < 5000)][['发放贷款日期','贷款金额']]
print(df1)