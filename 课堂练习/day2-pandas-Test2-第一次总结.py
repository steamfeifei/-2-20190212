import numpy as np
import pandas as pd

# ---常用的数据类型：
# Series  序列
# DataFrame   数据框

#==== Series
# 创建Series
pd1 = pd.Series(np.arange(0, 10), index=np.arange(10))
print(pd1)

pd2 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4}, index=['a', 'b', 'd', 'f'])
print(pd2)

# 获取Series 数据
print(pd2.a)
print(pd2['a'])
print(pd2[0])
print(pd2[1:5:2])
print(pd2[['a', 'b', 'f']])
print(pd2['a':'f'])
# Series 数据的比较
print('b' in pd2)
print(0 in pd2)
print(pd2 > 0)
print(pd2[pd2 > 1], type(pd2[pd2 > 2]))

# 常用 属性  和 方法
print(pd2.index)
print(pd2.values)
pd2 = pd2.map(lambda x : x + 1)
print(pd2)

# ---- DataFrame
pd3 = pd.DataFrame(np.arange(24).reshape((6, 4)), index=[1, 2, 3, 4, 5, 6], columns=['a', 'b', 'c', 'd'])
print(pd3)

dict1 = {
    'a': [1, 2, 3, 4],
    'b': [1, 2, 3, 4],
    'c': [1, 2, 3, 4],
    'd': [1, 2, 3, 4],
}
pd4 = pd.DataFrame(dict1, index=[1, 2, 3, 4], columns=dict1.keys())
print(pd4)

# 获取 DataFrame 数据
print(pd4.a, type(pd4.a))   # 直接获取的是列的数据
print(pd4['a'])
print(pd4[0:2])
print(pd4[1:2])

# 通过标签获取
pd5 = pd.DataFrame(np.arange(12).reshape((4, 3)), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C'])
print(pd5)
print(pd5.loc['a':'d', 'A':'B'])
print(pd5.loc['a', ['A','C']])
print(pd5.loc[:, ['A', 'C']])
print(pd5.loc[['a','b'],['A', 'B']])

# 通过位置获取
print(pd5.iloc[[1,2], :])
print(pd5.iloc[1:2, 1:2])
print(pd5.iloc[1, [1, 2]])

# 混合获取
print(pd5.ix[1:2, ['A', 'B']], type(pd5.ix[1:2, ['A', 'B']]))
print(pd5.ix[1, ['A']])
print(pd5.ix['a', 'A'], type(pd5.ix['a', 'A']))
print(pd5.ix[1, 1])

# 获取 属性  和  方法
print(pd5.index, type(pd5.index))
print(pd5.columns, type(pd5.columns))
pd5.index.name = '小写'   # 索引名
pd5.columns.name = '大写'     # 列名
print(pd5)
print('----pd5----\n', pd5.T)

# 判断
print(pd5.A)
print(pd5.A > 5)
print(pd5.A[pd5.A > 5])

# 删除
# del pd5['A']
# print(pd5)
pd5.drop(['A'], axis=1, inplace=False); print(pd5)
print(pd5.drop(['A'], axis=1, inplace=False)); print(pd5)
# pd5.drop(['a'], axis=0, inplace=False); print(pd5)
# print(pd5.pop('A'))
# print(pd5)

# 插入数据
pd5.insert(1, 'G', pd5['A'])
print(pd5)
pd5.insert(1, 'F', [1, 2, 3, 4])
print(pd5)
#--插入行数据
pd5 = pd5.append(pd.Series([1, 2, 3, 4, 5], index=['A', 'F', 'G', 'B', 'C']), ignore_index=True)
pd5.iloc[4] = pd.Series([1, 2, 3, 4, 6], index=['A', 'F', 'G', 'B', 'C'])
print(pd5)

# -- 替换数据
print('---替换数据----')
print(pd5)
pd6 = pd5.replace(1, np.nan, inplace=False)     # 替换数据
print(pd6)

# 处理 NaN 数据
pd6 = pd.DataFrame(np.arange(12).reshape((4, 3)), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C'])
pd6.iloc[1, 2] = np.nan
pd6.iloc[2, 2] = np.nan
print(pd6)
pd7 = pd6.dropna(axis=0, how='any')
print(pd7)
pd7 = pd6.fillna(0)
print(pd7)
pd7 = pd6.isnull()
print(pd7)
print(pd6.values)
print(pd7.values)
print(pd6.values[pd7.values])
print(np.any(pd7))  # 有 true 就为 true
print(np.all(pd7))  # 有 false 就为 false

# 常用方法
print(pd6.dtypes)   # 每一列的数据类型
print(pd6)
print(pd6.describe())   # 数据描述
print(pd6.sum())    # 求和
print(pd6.var())    # 求方差
print(pd6.std())    # 求标准差
print(pd6.skew())   # 求偏度，偏离标准正太分布
print(pd6.kurt())   # 求峰度
print(pd6.median()) # 求中位数
print(pd6.sort_values(by=['A', 'B'], ascending=[False, True]))  # 对数据集排序， 单例默认升序

#-- 去重
pd8 = pd.DataFrame(
    [
        [1, 2, 3, 5],
        [1, 3, 3, 5],
        [1, 2, 3, 5],
        [1, 4, 3, 5],
    ], index=['a', 'b', 'c', 'd'], columns=['k1', 'k2', 'C', 'D']
)
print(pd8)
pd9 = pd8.drop_duplicates(inplace=False)    # 某一行与另外一行完全相同时，去掉其中一行
print(pd9)
pd8['k1'] = pd8['k1'].drop_duplicates()     # 只去掉k1相同的行中元素，并且赋值为NaN
print(pd8)
pd9 = pd8.drop_duplicates(subset='k1', inplace=False)   # 根据k1去重，去掉重复的元素所在的行，只保留一个元素行
print(pd9)

# --- 文件的 读取  和 输出
# import os
# os.chdir('E:\JJJJJQQQQXXXXIIIII2\机器学习222222\课堂练习')
# file = pd.read_excel('房天下.xls')
# print(file)
# file.to_excel('gaofei.xls', sheet_name='gaofei')    # 保存为表格文件


# 众数
print(pd8)
print(pd8['k2'].value_counts())     # 频数统计
# import scipy.stats import mode # 科学计算包计算众数模块
print(pd8['k2'].tolist())


# 计算新列
pd8['E'] = pd8['C'] / pd8['D']
print(pd8)

# 删除多行 / 多列
pd9 = pd8.drop(labels=['a', 'b'], inplace=False, axis=0)
print(pd9)
pd9 = pd8.drop(labels=['D', 'C'], inplace=False, axis=1)
print(pd9)

data4 = pd.DataFrame(np.arange(12).reshape((3, 4))
                ,index=['Ohio', 'Colorado', 'New York'],
                columns=['one', 'two', 'three', 'four'])
print(data4)
data4.index = data4.index.map(str.lower)
print(data4)
data4.index = data4.index.map(str.upper)
print(data4)
data4.columns = data4.columns.map(str.title)
print(data4)
data4.rename(index={'OHIO':'aaa'}, columns={'One':'11'}, inplace=True)  # 修改行名和列名
print(data4)
data4.reset_index(inplace=True)     # 重置索引为默认 0  1  2  、、、
print(data4)
data4.index.name = '行'      # 命名索引名
print(data4)

# -- pandas 分箱操作 -------------
# pandas.cut 小结
# pandas.cut(x, bins, right=True, labels=None, retbins=False, precision=3,
#         include_lowest=False, duplicates='raise')
# 切割一维的数组，如连续的年龄segment成年龄段
# x:一维的数组
# bins：int，标量的序列，pandas的intervalindex
# right：Boolean默认是True，表示范围包含右边缘的值否
# labels：数组，bool，任意值，返回值的label
# retbins：返回bins与否，当bins是标量时无效
# precision：展示bins的数量
# include_lowest:分开的是左闭合区间与否
# duplicates:If bin edges are not unique, raise ValueError or drop non-uniques.

ages = [10, 20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]     # 如果数据不在分箱区间内，则为 NaN
bins = [18, 25, 35, 60, 100]
labels = ['young','a','b','old']
age1 = pd.cut(ages, bins, labels=labels)
print(age1)

# 分组统计
df1 = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'age' : [12,30,45,20,50],
                   'weight' : np.random.randn(5)}, index=[1, 2, 3, 4, 5])
print(df1)
print(df1.groupby(by=df1['key1'])['age'].mean())
print(df1.groupby(by=df1['key1'])['age'].max())
print(df1.groupby(by=df1['key1'])['age'].mean())
print(df1.groupby(by=df1['key1']).mean())   # 计算可计算的列的平均值

# ------   分组
dict10 ={'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
pd10 = pd.DataFrame(dict10)
print(pd10)

# 拆分组
print(pd10.groupby('Team'))
groups = pd10.groupby('Team')
print(groups.groups)    # 所有分组
print(groups.ngroups)   # 分组数
groups = pd10.groupby(['Team', 'Year'])
print(groups.groups)
print(groups.ngroups)   # 分组数
groups = pd10.groupby('Year')
print(groups)   # 每个元素中第一个元素为分组数据，第二个元素为分组对应的数据框

for i,j in groups:
    print(i,j)

print(groups.get_group(2014))   # 选择人一个组

#  聚合
print(groups['Points'].agg(np.mean))
print(groups.agg(np.size))      # 查看每个分组大小的方法

print(groups['Points', 'Rank'].agg([np.sum, np.mean, np.std]))


# query  学习
d={
    'name':['xiao','dan','qi'],
    'sex':['male','female','male'],
    'age':[23,24,24]
}
pd11 = pd.DataFrame(d)
print(pd11)
print(pd11.query('name == "xiao"'))


# 表连接 合并
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print(left)
print('==========')
print(right)
#  merge  合并
print(pd.merge(left, right, on='id'))
print(pd.merge(left, right, on=['id', 'subject_id'], how='left', indicator=True, suffixes=['_left',  '_right']))
print(pd.merge(left, right, on=['id', 'subject_id'], how='outer', indicator=True, suffixes=['_left',  '_right']))
print(pd.merge(left, right, on=['id', 'subject_id'], how='right', indicator=True, suffixes=['_left',  '_right']))
print(pd.merge(left, right, on=['id', 'subject_id'], how='inner', indicator=True, suffixes=['_left',  '_right']))
# concat 合并
print('=============')
print(pd.concat([left, right], axis=1, join='outer', join_axes=[left.index]))   # join_axes  合并列，代表行标签，反之为列标签
print('=============')
print([left.columns[:2]])

print(right)
print(right[(right.id > 2)])