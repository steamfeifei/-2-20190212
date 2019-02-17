import numpy as np
import pandas as pd

# title1
# 背景：数据清洗是数据机器学习中重要的流程之一，数据建模的效果好坏，很大程度上依赖于数据清洗的质量，本案例是银行风控项目中，数据预处理部分的需求，具体要求如下：
# 要求：
# 1. 读入bank数据表，删除列，列名为每月归还额（10分）
# 2. 对指定列做频数统计，列名为贷款期限（10分）
# 3. 对指定列做分组统计，列名为还款状态。在此基础上，计算各分组贷款金额列的均值（8分）
# 4. 统计贷款金额的均值、最小值、最大值、中位数、方差（6分）
# 5. 对数据进行排序，按照发放贷款日期（降序）贷款金额（升序）排序（6分）
# 6. 按照贷款金额除以贷款期限计算生成新列，并命名为每月归还额（5分）
# 7. 提取行（账户号在3000到4500之间）列（发放贷款日期和贷款金额）数据框（3分）

# data = pd.read_excel('bank.xls')
# print(data)
#
# print(data['贷款期限'].value_counts())
# print(data.groupby(by='还款状态')['贷款金额'].mean())
# print(data['贷款金额'].mean())
# print(data['贷款金额'].min())
# print(data['贷款金额'].max())
# print(data['贷款金额'].median())
# print(data['贷款金额'].var())
# # data = pd.DataFrame()
# print(data.sort_values(by=['发放贷款日期', '贷款金额'], ascending=[False, True]))
# print(data[(data['账户号'] >= 3000) & (data['账户号'] <= 4500)])

# title2
# 已知有如下数据集X，求此数据集的协方差矩阵并打印输出。
# X = [[2, 0, -1.4],
#     [2.2, 0.2, -1.5],
#     [2.4, 0.1, -1],
# [1.9, 0, -1.2]]
# X = [[2, 0, -1.4],
#     [2.2, 0.2, -1.5],
#     [2.4, 0.1, -1],
# [1.9, 0, -1.2]]
# print(np.cov(X, rowvar=True))

# title3
# Fisher1936年收集了三种鸢尾花分别50个样本数据（Iris Data）：Setosa、Virginica、Versicolour。解释变量是花瓣（petals）和萼片（sepals）长度和宽度的测量值，响应变量是花的种类。鸢尾花数据集经常用于分类模型测试，scikit-learn中也有。
# 题目要求：
# 1.把iris数据集降成方便可视化的二维数据（10）
# 2.打印主成分的方差解释率（5分）
# 3.降维后的数据在二维空间可视化（3分）

from sklearn.datasets import  load_iris
data = load_iris()
dataX = data.data
data_columns = data.target_names
target = data.target
print(data)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
# print(pca.fit_transform(dataX))
# print(pca.explained_variance_ratio_)
dataX_Dec = pca.fit_transform(dataX)
import matplotlib.pylab as plt

# print(data_columns)
for color, classification, target_name in zip('rgb', [0, 1, 2], data.target_names):
    plt.scatter(dataX_Dec[target==classification, 0], dataX_Dec[target==classification, 1], c=color, label=target_name)

plt.show()