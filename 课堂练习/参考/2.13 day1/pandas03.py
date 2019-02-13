import numpy as np
import pandas as pd
#1.带行索引的一维数组（注意：rand()和randn()的区别）
# numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值。
# numpy.random.rand(d0, d1, …, dn)的随机样本位于[0, 1)中
# Series1=pd.Series(np.random.randn(4))
# print(Series1)
#2.map借鉴了python的内置函数map，是panadas的方法，是series1数据对象的map
# lambda x:round(x)+3：对于每个输入的元素x，四舍五入+3，重新给series1里的元素赋值
# Series1 = Series1.map(lambda x:round(x)+3)
# print(Series1)
# list = [1,2,3,4]
# for i in map(lambda x:x*x,list):
#     print(i)
# def f(a):
#     return a*a
# for i in map(f,list):
#     print(i)

# 4.list转一维series
# li = ['Tokyo','Seoul','Beijing']
# # # 直接转，默认索引为0、1、2、3...
# Series4=pd.Series(li)
# print(Series4)
# # # 转series时加索引值
# Series5=pd.Series(li,index=['Japan','S.Korea','China'])
# print(Series5)
# Series4.to_csv('s4.csv')#转成csv格式

# # 5.多维数组转化成dataframe格式
# dataNumpy=np.asarray([('Japan','Tokyo',4000),
#                       ('S.korea','Seoul',1300),
#                       ('China','Beijing',9000)])
# df1=pd.DataFrame(dataNumpy,columns=['nation','capital','GDP'])  #转dataframe格式时加列名
# print(df1)
# df1.to_excel('df1.xls',sheet_name='b') #工作簿的名字是a
# print(df1.index)   #打印结果：RangeIndex(start=0, stop=3, step=1)
# df1.index.name = 'id' #给索引命名
# print(df1.columns)   #打印结果：Index(['nation', 'capital', 'GDP'], dtype='object')
# df1.columns.name = 'country'  #给列名设置名字
# print(df1)
# df1.to_excel('df2.xls',sheet_name='b')

# # 6.字典转化成dataframe格式 ,最为常用的一种方式，键变为列名了
# Dict={'nation':['Japan','S.korea','China'],
#       'capital':['Tokyo','Seoul','Beijing'],
#       'GDP':[4900,1300,9000]}
# df2=pd.DataFrame(Dict)
# print(df2) #python版本不同，打印列的先后顺序可能会不一样
#
# # #7.截取行或列
# print('-------------1.切行-------------------')
# print(df2[0:2])   #包前不包后
# print('-------------2.切列-------------------')
# print(df2['nation'])   #方法一：用列名
# print(df2.iloc[:,0])  #用数字切时“必须”要用iloc切片器
# #
# #8.切片器  都没有步长，没有numpy强大一些
# # （1）iloc切片器：([:,0]: ','前表示行  ','后表示列 ；此切片的意思是切出所有行的第1列)
# print('-------------3-------------------')
# print(df1.iloc[0:2,:])    #第1、2行的所有列
# print('-------------4-------------------')
# print(df1.iloc[0:2,1:3])  #第1、2行的2、3列
# # （2）loc切片器：[[0,1],:]间括号的内容只能用行名（如索引为a,b,c,也就是说按照实际的行索引或者列名来切）
# #  或者列名表示，用'，'隔开
# print('-------------5-------------------')
# print(df1.loc[[0,1],:])
# print(df1.loc[[0,1],['capital','GDP']]) #此行代码与上面4等价
# # （3）ix切片器:iloc和loc的综合使用，不常用了
# print('-------------6-------------------')
# print(df1.ix[0:2,'nation'])

# # 9.新增一列，列名为'region'，值为East_Asian
# df2['region']='East_Asian'
# df2['region']=['East_Asian','a','b']  #给新增列添加不同的值是用数组表示
# print(df2)

# 10.新增一行
# new=pd.DataFrame({'nation':'UA',
#                   'capital':'HT',
#                   'GDP':4000,
#                 'region':'Africa'},index=['a'])
# print(new)
# # index=[2]表示添加索引值名称为2，也可以设置为字符类型，必须设置
# df1 = new.append(new,ignore_index=False)# ignore_index=True忽略索引，为true时设置的索引不起作用,索引就是行标
# print(df1)

#11.删除
# 有两种方式
# # del ['列名称'，'列名称']  删除列的所有行
# df1.drop(['GDP','region'],axis=1,inplace=True)  #axis=1对列操作,inplace=True：替换原文件，更新
# df1 = df1.drop([1],axis=0)    #axis=0对行操作  需要用df1接一下
# print(df1)
# del df1['GDP']
# del df1['region']

# #12.修改
# df1.iloc[1:3,2]=[2000,1000]  #iloc须使用数字索引
# print(df1)
