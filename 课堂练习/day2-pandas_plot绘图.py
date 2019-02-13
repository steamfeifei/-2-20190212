import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000), index=np.arange(1000))
print(data)
data = data.cumsum()    # 累加
print(data)
data.plot()
plt.show()

data1 = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=['A', 'B', 'C', 'D'])
print(data1)
data1 = data1.cumsum()
print(data1.head())     # 打印前5行
data1.plot()
plt.show()
ax = data1.plot.scatter(x='A',  y='B', color='Blue', label='class 1')
data1.plot.scatter(x='A', y='C', color='Red', label='class 2', ax=ax)   # ax 表示画在同一个画布中
plt.show()
