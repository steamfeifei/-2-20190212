import pandas as pd
import numpy as np
# from sklearn.preprocessing import Imputer     # 数据预处理--填补缺失值方法类
# from sklearn.preprocessing import LabelEncoder    # 字符编码
# from scipy.stats import mode    # 科学计算包计算众数模块

# series1 = pd.Series(list(range(5)))  #创建数组Series 0,1,2,3,4，索引也是0,1,2,3,4
# print(series1)
# series12 = series1.map(lambda i:i+1) # map 是series的一个方法
# print(series12)
data = pd.DataFrame(
        {'h':pd.Series(['male','female','male','female']),
         'age':pd.Series([20,21,22]),
         'weight':pd.Series([50,50,40,70])} #键作为了列名  不再是行索引，与上节课中值用list情况不同
        )
print(data)
# #
# print('-----转置-------') #同一列必须是相同的数据类型，转置后有字符型的列强制都把数据转成了字符型
dataT = pd.DataFrame(data.T)
print(dataT)
print(dataT.dtypes)   #打印每一列的类型
#
# # ——————
# # print('-----打印列名-------')
print(data.columns)
print(dataT.columns)
# # # print('---新建列----')
data['weight+1'] = data['weight'] + 10
dataT['4'] = dataT[1]
print(data)
print(dataT)
# # # 描述性分析
print(data.describe())
print(data.sum())     #求和
print(data.var())     #方差
print(data.std())     #标准差
print(data.skew())   # 偏度：偏离标准正态分布
print(data.kurt())   # 峰度
print('---排序----')
print(data.sort_values(by=['weight','age'],ascending=[False,True]))  #对数据集排序单列默认升序
data1 = pd.DataFrame({'k1': ['b','b',np.nan,'a','b','a','b'],
                        'k2': [3,np.nan , 1, 3, 3, 4, 4]})

print(data1)# NaN为浮点型，所以每一列都变成了浮点型，# pandas 中每一列数据类型必须一样
# print('---去重----')
data1.drop_duplicates(inplace=True)   # 多列：某一行和另一行完全相等时去其中一行
data1['k1'] = data1['k1'].drop_duplicates()  # 单列：根据k1 去重，只去k1相同的赋值为nan 保留k2
print(data1)
print(data1.drop_duplicates(subset='k1')) # 单列：只根据k1 去重，k1相同的只保留1行，剩下的连k2一起删掉
# print('----处理缺失值-----')
# print(data1.dropna())   # 剔除缺失值
# print(data1.fillna('three'))   # 填补缺失值
# print(data1.fillna(data1.mean()))   # 均值处理
# print(data1.fillna(data1.median()))   # 中位数处理

# 众数填补缺失值
# print(data1['k1'].value_counts())   # 频数统计
# print(mode(data1['k1'].tolist()))    # 计算众数，计算list 里哪个元素出现次数最多
# print(data1.fillna('b'))   # 填补缺失值
#方法二（自学）------------------------------------------------
# model = Imputer(strategy='most_frequent',axis=1) #初始化对象 因为Imputer是一个方法类
# model.fit(data1['k1'])
# data1['k1'] = model.transform(data1['k1']) #转换成新的数据集  数据列
# print()
#————————————————————————————
# 计算新列
# df = pd.DataFrame({'data1' : np.random.randn(5),    # 标准正态分布     均值为0 标准差为1
#                    'data2' : np.random.randn(5)})
# print(df)
# df['ratio'] = df['data1'] / df['data2']
# print(df)
# 删除多列
# df = df.drop(labels=['data1','data2'],axis=1)
# # print(df)
# # 删除多行
# df = df.drop(labels=[1,3])#删除标签是1和标签为3的行
# print(df)
# 替换
# data3 = pd.Series([1., -999., 2., -999., -1000., 3.])
# print(data3)
# data3.replace(-999, np.nan, inplace=True)#用空值代替-999
# print(data3)
# data3.replace([-999,-1000], np.nan, inplace=True) #多个值替换
# print(data3)
# 修改索引名、列名
# data4 = pd.DataFrame(np.arange(12).reshape((3, 4))
#                     ,index=['Ohio', 'Colorado', 'New York'],
#                     columns=['one', 'two', 'three', 'four'])
# print(data4)
# data4.index = data4.index.map(str.upper)
# print(data4)
# data4.columns = data4.columns.map(str.title)
# print(data4)
# data4.rename(index={'Ohio':'Hio'},columns={'three':'five'},inplace=True)  #修改行名和列名
# print(data4)
# data4['five'] = data4['five'] - 1
# print(data4)
# 重置索引
# # print(data4)
# data4.reset_index(inplace=True)# 索引下标按照默认的0,1,2
# print(data4)
# data4.rename(index={1:'a'},inplace=True) #索引下标为1的行的索引重置为索引a
# data4.index.name = '1'#为索引列命名
# print(data4)

#分箱操作（数据离散化）
# ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# print(ages)
# bins = [18, 25, 35, 60, 100]
# labels = ['young','a','b','old']
# age1 = pd.cut(ages,bins,labels=labels)
# print(age1)

# 分箱操作（数据离散化）例二
# data5 = pd.read_excel(r'D:\大纲\考试题\1511R\大数据_1511R（数据挖掘）_01_单元\aviation.xlsx',
#                       index_col='MEMBER_NO')
# print(data5.head())
# print(data5.info())
# data5['age'] = data5['age'].dropna()
# data5['age'] = pd.cut(data5['age'],bins=[0,30,50,data5['age'].max()],
#                       labels=['young','middle','old'])
# print(data5['age'].value_counts())    # 频数统计
#

# df1 = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
#                    'key2' : ['one', 'two', 'one', 'two', 'one'],
#                    'age' : [12,30,45,20,50],
#                    'weight' : np.random.randn(5)})
# print(df1)
# # print('----------分组统计------------------')
# print(df1.groupby(by=df1['key1'])['age'].mean())
# # print(df1.groupby(by=df1['key1'])['age'].max())
# print(df1['age'].groupby(by=df1['key1']).mean())
# # print('----------------')
# # print(df1.groupby(by=df1['key1']).mean())
# # 切片
# dates = pd.date_range('20130101',periods=6)
# df3 = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
# # print(df3)
# # print(df3.iloc[:,:-1])
