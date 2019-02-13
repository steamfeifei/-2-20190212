import numpy as np
import pandas as pd


data = pd.read_excel('房天下.xls', sheet_name='数据源')
print(data.head())
data['月'] = pd.cut(data['月'], [1, 4, 7, 10, 13], right=False, labels=['第一季度', '第二季度', '第三季度', '第四季度'])
print(data)
a = data.query('年 == 2009 & 月 == "第三季度" & 销售区域 in ("北京","上海","广州")').groupby(by='销售区域')['销售数量'].sum()
print(pd.DataFrame(a))
print(a, type(a))

b = data.groupby(by=['年', '月'])['销售数量'].sum()
print(b, type(b))
import matplotlib.pylab as plt
c = pd.DataFrame(b)
print(c.columns)
print('----------')
plt.bar(range(len(b)),c['销售数量'])
plt.show()