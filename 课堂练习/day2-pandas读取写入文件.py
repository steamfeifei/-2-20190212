import numpy as np
import pandas as pd

file = pd.read_excel('房天下.xls')
# print(file,type(file))

file.iloc[:, 2] = '深圳'
print(file)

file.to_excel('gaofei.xls')
pd.read_