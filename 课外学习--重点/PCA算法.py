# 第一主成分就是从数据差异性最大（方差最大）的方向提取出来的
# 第二主成分就是从数据差异性次大的方向，并且要与第一个主成分方向正交

# PCA 降维的算法流程
#1、 数据预处理： 中心化 X - X.mean()
#2、 样本的协方差矩阵： 1/m * X.dot(X.T)
#3、 对协方差矩阵做特征值分解
#4、 选出最大的k个特征值对应的k个特征向量
#5、 将原始数据投影到选取的特征向量上
#6、 输出投影后的数据集
#7、 低维重构数据

import numpy as np
np.random.seed(3)
# 构建原始数据
Data =  [[9, 23, 32], [0, 1, 9], [3, 5, 58], [102, 58, 25], [5, 9, 5], [5, 21, 43]]
Data =  np.random.random([6,3]) * 3
newData = np.array(Data, dtype='float64')
newData -= newData.mean(axis=0)
newData /= newData.std(axis=0, ddof=1)
# newData -= newData.mean(axis=0)
# print(newData)

# 求该数据的协方差矩阵
# xfc = np.cov(newData, rowvar=0)
xfc = np.cov(newData.T)
# xfc = xfc * 5 / 6
# 求协方差矩阵的特征值 和 特征向量
eigVals, eigVects = np.linalg.eig(xfc)
# print(eigVals[[0, 2, 1]] / eigVals.sum()) # S
# print(eigVects[:,[0, 2, 1]]) # U
# print(eigVects)
print('='*100)

U, S, V = np.linalg.svd(np.array(newData))
# # print(np.linalg.svd(np.array(newData))[0])
# print(np.linalg.svd(np.array(newData))[1])
# print(np.linalg.svd(np.array(newData))[2])
# # print(np.linalg.svd(np.array(newData)))
print(U)
print(S / S.sum())
print(V.T) # UT
# print(U.dot(S * `V))
SS = np.eye(len(S)) * S
print(V.T.dot(SS).dot(V.T))

# from sklearn.decomposition import PCA
#
# pca_model = PCA()
# pca_model.fit(newData)
# # print(pca_model.explained_variance_)
# # print(pca_model.components_.T)
# a =  pca_model.transform(newData)
# # print(a)
# UT = pca_model.components_
# print(a.dot(UT))
# print('='*100)
# print(pca_model.inverse_transform(a))
# print('='*100)
# print(newData)

