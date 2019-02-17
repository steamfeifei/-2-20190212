import numpy as np
import matplotlib.pylab as plt

# 获取数据
np.random.seed(3)
data = np.random.randint(0, 100, (5, 2))
data = data.astype(float)
print('原数据为：\n', data)

# 求数据协方差矩阵
A = np.cov(data.T)

# 求数据的特征值 和  特征向量
eigVal, eigVet = np.linalg.eig(A)

# 获取降维后的数据
argindex = np.argsort(-eigVal)
top = 1
argindex = argindex[0:top]
print('特征值：\n', eigVal)
print('特征向量：\n', eigVet)
eigVet = eigVet[:, argindex]
print(eigVet)

print(data)
demData = data.dot(eigVet)
# demData = data.dot(eigVet)
print('降维后的数据为：\n', demData)

# 反向重构后的数据为:
reconsitution = demData.dot(eigVet.T)
print('重构后的矩阵为：\n', reconsitution)


# ===== 调用库函数
from sklearn.decomposition import PCA

pca = PCA(n_components=1)
print('调用库函数：\n', pca.fit_transform(data))
print(pca.components_)