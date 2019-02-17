import numpy as np

#  title1
A = [
    [2,	    0	,-1.4],
    [2.2,	0.2	,-1.5],
    [2.4,	0.1	,-1],
    [1.9,	0	,-1.2]
]
A = np.cov(A)
print(A)

# title2
a1 = [[1, -2], [2, -3]]
A = np.cov(a1)
U, S, V = np.linalg.svd(A)
print('特征值：',   S )
print('特征向量：', U )