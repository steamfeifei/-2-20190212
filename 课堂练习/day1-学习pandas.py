import numpy as np
import pandas as pd

s1 = pd.Series([4, 5, 6, 7])    # 创建一个Series, 索引为默认值
print(s1)

print(s1.values)    # Series的值
print(s1.index)     # Series的索引


s2 = pd.Series([4, 56, 6., -5], index=['d', 'b', 'a', 'c'])
print(s2)
print(s2['a'])  # 通过一个索引获取元素
print(s2[['a', 'b']])   # 通过多个索引获取元素
print('b' in s2)    # 判断b是否在s2中
print('e' in s2)
print('c' in s2)
#  Series 可以看成是一个定长的有序字典
dic1 = {'apple':5, 'pen':3, 'applepen':10}
s3 = pd.Series(dic1)
print(s3)

# DataFrame
data = {'year':[2014, 2015, 2016, 2017],
        'income':[1000, 11, 22, 333],
        'pay':[55, 55, 56, 12]
}
df1 = pd.DataFrame(data)    # 索引为默认索引
print(df1)

df2 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df2)

df3 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['a', 'b', 'c'], columns=[1, 22, 3, 76])
print(df3)
print(df3.columns)  # 列
print(df3.index)    # 行
print(df3.values)   # 值
print(df1.describe())   # 描述
print(df1.T)    # 行列互换， 转置
print(df3.sort_index(axis=1))  # 对列进行排序
print(df3.sort_index(axis=0))   # 对行进行排序
print(df1.sort_values(by='pay'))    # 对3的列进行排序

#----------------------------------
print('===============================')

dates = pd.date_range('20170101', periods=6)    # 日期
print(dates)
df1 = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df1)

print(df1['A'])     # 将DataFrame 的列获取为一个Series
print(df1.A)
print(df1[0 : 2])   # 获取前两行 0 ， 1
print(df1['20170102':'20170104'])   # 获取日期为 20170102 - 20170104 行的内容

# 通过标签选择数据
print('=======')
print(df1.loc['20170102'])  # 提取对应的行
print(df1.loc['20170101', ['A', 'C']])  # 提取行 以及 对应的列
print(df1.loc[:, ['A', 'C']])
print(df1.loc['20170101', ['A', 'C']])

#  通过位置选择数据
print(df1.iloc[2])  # 获取行下标为2的数据
print(df1.iloc[1:3, 2:4])   #  获取行列数据
print(df1.iloc[[1, 2, 4], [1, 3]])  # 单独获取行，列

# 通过混合标签位置选择
print(df1.ix[2:4, ['A', 'C']])
print(df1.ix['20170101':'20170103',2:4])
print(df1.A > 6)    #  选出数据并判断
print(df1[df1.A > 6])   # 只保留值为true的行

# pandas的赋值 和 操作
print('pands的赋值 和 操作')

dates = np.arange(20170101, 20170107)
df1 = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df1)
print(df1.iloc[2, 2])
df1.iloc[2, 2] = 100    # 对第二行第二列的值进行赋值
print(df1)
df1.loc[20170102, 'B'] = 300
print(df1)
df1[df1.A > 10] = 0
print(df1)
df1.A[df1.A == 0] = 1   # 对某一列的某几行赋值
print(df1)

df1['E'] = 10   # 添加一列数据
print(df1)
df1['F'] = pd.Series([1, 2, 3, 4, 5, 6], index=dates)  # 在DataFrame 中 每一列相当于一个Series,对应的索引必须一致
print(df1)

df1.loc[20170107, ['A', 'B', 'C']] = [1, 2, 3]  # 添加一行， 可以指定列
print(df1)
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=['A', 'B', 'C', 'D', 'E', 'F'])
s1.name = 'S1'
df2 = df1.append(s1)
print(df2)
df1.loc[20170108, :] = s1
print(df1)

df1.insert(1, 'G', df2['E'])    # 在第一列插入索引为G的df2中的E列
print(df1)
g = df1.pop('G')    # 弹出G列
df1.insert(6, 'G', g)   # 在最后插入G列
print(df1)
del df1['G']    # 删除G列
print(df1)
df1.pop('F')
print(df1)
df2 = df1.drop(['A', 'B'], axis=1)    # 删除 A , B 列,将删除后的的值赋值给df2，对df1并没有做改变
print(df2)
df3 = df1.drop([20170101, 20170102], axis=0)    # 删除 行，赋值同上
print(df3)
