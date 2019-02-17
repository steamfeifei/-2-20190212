import numpy as np
import matplotlib.pylab as plt

# 获取数据
np.random.seed(3)
data = np.random.randint(1, 20, (6, 2))
data = data.astype(float)
print(data)

# 数据的中心化
data_mean = data.mean(axis=0)
# data -= data_mean

# 求协方差矩阵
A = np.cov(data.T)  # 内部已经去中心化了
# print('协方差矩阵：\n', A)

# 求特征值 和 特征向量
eigVal, eigVect = np.linalg.eig(A)
# print('特征值：\n', eigVal)
# print('特征向量：\n', eigVect)

# 求原矩阵在低维空间的映射
eigValsSort = np.argsort(-eigVal)       # 降序排序
top = 2
eigValsSort = eigValsSort[0:top]
eigVect = eigVect[:, eigValsSort]
# print(eigValsSort)

# 高维 转 低维度
lowData = data.dot(eigVect)
# print('转换后的低维：\n', lowData)

# 低维 重构数据
reconsitution = lowData.dot(eigVect.T)
# print('重构后的数据：\n', reconsitution - 0.5 * np.mean(reconsitution, axis=0))
print('重构后的数据：\n', reconsitution)
# print('重构后的数据：\n', reconsitution + data_mean)

# ====================调用库函数
from sklearn.decomposition import PCA

pca = PCA(n_components=1)
print(pca.fit_transform(data))
