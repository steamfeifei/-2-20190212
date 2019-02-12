import numpy as np
import pandas as pd

s1 = pd.Series([1, 2, 4, 5]); print(s1)
print(s1[0])
print(s1[1:5], type(s1[1:5]))
print(s1.values)
print(s1.index)
index = [ i for i in s1.index]; print(index)

s2 = pd.Series([4, 2, 5, 6], index=['a', 'b', 'c', 0]); print(s2)
print(s2['a':'b'], '-----------------')
print(s2['a'])
print(s2[['a', 'b', 0]], '===========')
print(s2[0])
print('b' in s2)
print(s2 > 3)
dic1 = {'aaa':3, 'bbb':44, 'dddd':111}
s3 = pd.Series(dic1)
print(s3)
s4 = pd.Series(dic1, index=['aaa', 'bbb', 'cc', 'dddd'])
print(s4)

print('===========DataFrame==========')
data = {'year':[2014, 2015, 2016, 2017],
        'income':[100, 200, 500, 300],
        'pay':[55, 51, 52, 11]
}
df1 = pd.DataFrame(data, index=['a', 'b', 'c', 'd'], columns=['year', 'pay', 'income'])
print(df1)

df2 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df2)

df3 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['b', 'c', 'a'], columns=['year', 'pay', 'income', 'gaofei'])
print(df3)

# 获取数据
print(df3.index)
print(df3.values)
print(df3.columns)
print(df3.describe())
print(df3.T)
print(df3.sort_index(axis=0))
print(df3.sort_index(axis=1))
print(df3.sort_values(by='a',axis=1))

# 获取数据高级
dates = pd.date_range('20170101', periods=6); print(dates)
df4 = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df4)

# 选择DataFrame, 获取数据
# --- 如果获取的元素为单个元素，或者元素数组，那么 获取的就是对应的列的数据
# -- 如果获取的元素为0:2 切片数据， 获取的数据为行的数据
print(df4['A'])
print(df4.A)
print(df4[0 : 1], '======================')
print(df4['20170101':'20170104'])

# 通过标签获取 一行的数据; 或者几行几列的数据
print(df4.loc['20170102'])
print(df4.loc['20170102', ['A', 'C']])
print(df4.loc[:, ['A', 'C']])

# 通过位置选择数据
print(df4.iloc[2], type(df4.iloc[2]))      # 获取行下标为2的数据
print(df4.iloc[1:3, 2:4])
print(df4.iloc[[1, 2, 4], [1, 3]])

# 通过混合标签位置选择
print(df4.ix[2:4, ['A', 'C']])
print(df4.ix['20170101':'20170104', 2:4])
print(df4.ix['20170101':'20170104'])

# 判断
print(df4.A , type(df4.A))      # 每一列为一个Series
print(df4.A > 0, type(df4.A > 0))       # 也是Series 类型
print(df4[df4.A > 0])

# 赋值
df4.loc['20170101'] = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
print(df4)
df4['A'] = pd.Series([1, 2, 5, 5, 5, 5], index=['20170101', '20170102', '20170103', '20170104', '20170105', '20170106'])
print(df4)
df4.loc['20170101', 'A'] = 200
print(df4)
df4.iloc[0, 0] = 100
print(df4)
df4.ix['20170101', ['A', 'B']] = 500
print(df4)
print(type(df4.ix['20170101', ['A', 'B']]))
print(type(df4.ix['20170101':'20170102', ['A', 'B']]))
print(type(df4.iloc[[1, 2, 4], [1, 3]]))
print(type(df4.loc['20170102':'20170102', ['A', 'C']]))

df4['A'] = 250
print(df4)
df4['F'] = pd.Series(np.arange(0, 6), index=dates)
print(df4)
# df4[0:1] = pd.DataFrame(np.arange(0, 5).reshape(1, 5), columns=['A', 'B', 'C', 'D', 'F'],index=['20170101'])
# print(df4)
df4.ix['20170101',:] = [1, 2, 3, 4, 5]
print(df4)
g = pd.Series([1, 2, 3, 3, 3], index=['A', 'B', 'C', 'D', 'F'])
g.name = 's1'
df4 = df4.append(g)
print(df4)

df4.insert(1, 'G', df4['A'])
print(df4)
g = df4.pop('G')
df4.insert(5, 'G', g)
print(df4)
del df4['G']
df5 = df4.drop(['A'], axis=1)
print(df5)




