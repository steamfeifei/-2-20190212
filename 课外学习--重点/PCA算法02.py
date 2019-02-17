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
import matplotlib.pylab as plt

np.random.seed(3)
data = np.random.randint(1, 12, (50, 2))
new_data = data.astype(float)
print(new_data)
#------------------
plt.scatter(data[:,0], data[:,1], c='b', marker='.')
#------------------
# 数据中心化
mean_val = new_data.mean(axis=0)
new_data -= mean_val

# 求协方差矩阵
A = np.cov(new_data.T)
print(A)

# 求特征值 和  特征向量
eigVals, eigVects = np.linalg.eig(A)
print(eigVals)
print(eigVects)

# 求原矩阵的映射
eigValsIndice = np.argsort(eigVals)
print(eigValsIndice)
top = 1
eigValsIndice = eigValsIndice[-1 : -(top + 1) : -1]
eigVects = eigVects[:, eigValsIndice]
print(eigVects)

# 高维 转 低维度
lowData = new_data.dot(eigVects)
print(lowData)

# 低维 重构数据
reconsitution = lowData.dot(eigVects.T) + mean_val
print(reconsitution)
#--------------
plt.scatter(reconsitution[:,0], reconsitution[:,1], c='r', marker='.')
#--------------
plt.show()



#===========调用库函数实现降维======================================
from sklearn.decomposition import PCA

pca = PCA(n_components=1)
print(pca.fit_transform(new_data))
