"""
读取ftx.xlsx表，其中包括了房天下网站从2009年1月到2010年12月的各大城市销售数据。
要求：
1.使用所学知识，从数据源中选择2010年第3季度北上广三个城市的销售数量总和，建立新表。
2.按照2009年和2010年的第1、2、3、4季度共8个时间节点，画出各节点对应销售数量总和的条形图。
"""
import pandas as pd
# import numpy  as  np
import matplotlib.pyplot as plt
import os
os.chdir(r'C:\Users\Lenovo\PycharmProjects\untitled\dm\数据挖掘\01Excel数据分析')
data = pd.read_excel('ftx.xlsx')
data = pd.DataFrame(data)
print(data.head())
a = data.query("年 == 2009 & 月 in (4,5,6) & 销售区域 in ('北京','上海','广州')").groupby(by='销售区域')['销售数量'].sum()
a = pd.DataFrame(a)#以数据框形式展现 否则以数组形式展现
print("----------")
print(a)
print("----------")
# qu询 ，后面只支持string形式的值，所以后面有“”ery，查
# 把月划分为等距的区间cut()函数
data['月'] = pd.cut(data['月'], [1,4,  7, 10, 13], right=False, labels=['第一季度', '第二季度', '第三季度', '第四季度'])
print(data)
last = data.groupby(by=['年', '月'])['销售数量'].sum() #按照年和月分组
print(last)
plt.bar(range(len(last)),last)
plt.show()

#1
#cut()
# cut(x,bins,right=True,labels=None,retbins=False,precision=3,include_lowest=False)
'''需要将数据值分段并排序到bins中时使用cut。 
此函数对于从连续变量转换为离散变量也很有用。 例如，cut可以将年龄转换为年龄范围组
x: 进行划分的一维数组
bins : 
1,整数---将x划分为多少个等间距的区间
2,序列—将x划分在指定的序列中，若不在该序列中，则是NaN
right : 是否包含右端点
labels : 是否用标记来代替返回的bins
retbins: 是否返回间距bins
precision: 精度
include_lowest:是否包含左端点
 
'''
# matplotlib.pyplot.bar(left, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)
# 绘制条形图。绘制带有矩形边界的条形图通过如下设置：
# left, left + width, bottom, bottom + height
# (left, right, bottom and top edges)
# 输入参数：
# left：标量序列。表示条形图左边x坐标。
# height：标量或者标量序列。条形图的高度。
# width：标量或者数组，可选参数。条形图宽度默认为：0.8。
# bottom：标量或者数组，可选参数。条形图y坐标，默认值为None。
# color：标量或者数组，可选参数。条形图前景色。
# edgecolor：标量或者数组，可选参数。条形图边界颜色。
# linewidth：标量或者数组，可选参数。条形图边界宽度。
# ---------------------

# ---------------------
