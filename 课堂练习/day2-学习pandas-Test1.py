import pandas as pd
import numpy as np

dates = np.arange(20170101, 20170105)
df1 = pd.DataFrame(np.arange(12).reshape((4, 3)), index=dates, columns=['A', 'B', 'C'])
print(df1)

df2 = pd.DataFrame(df1, index=dates, columns=['A', 'B', 'C', 'D', 'E'])
print(df2)

s1 = pd.Series([3, 4, 6], index=dates[:3])
s2 = pd.Series([33, 44, 55], index=dates[1:])
df2.D = s1
df2.E = s2
print(df2)

df3 = df2.dropna(axis=0, how='any')   # axis = 0 , 1, 0为行，1为列， how=['how', 'any'],任意一个或者多个all
                                # 删除行或者列中有NaN值的行或列
print(df3)

df4 = df2.dropna(axis=1, how='any')
print(df4)

df5 = df2.fillna(value=0)   # 把控制赋值为value的值
print(df5)

print(df2.isnull())     # 查看各个位置是否是空值
print(np.any(df2.isnull()))     # 如果有true，为true
print(np.all(df2.isnull()))     # 如果有false, 为false
