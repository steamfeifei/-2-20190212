import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.arange(12).reshape((3, 4)), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.arange(12, 24).reshape((3, 4)), columns=['A', 'B', 'C', 'D'])
df3 = pd.DataFrame(np.arange(24, 36).reshape((3, 4)), columns=['A', 'B', 'C', 'D'])

print(df1)
print(df2)
print(df3)

df4 = pd.concat([df1, df2, df3], axis=0)    # 纵向合并
print(df4)

df5 = pd.concat(([df1, df2, df3]), axis=0, ignore_index=True)   # 纵向合并， 不考虑原来的index
print(df5)

df6 = pd.concat([df1, df2, df3], axis=1)
print(df6)

#---------------------------
df2 = pd.DataFrame(np.arange(12, 24).reshape((3, 4)), columns=['A', 'B', 'C', 'F'])
df3 = pd.DataFrame(np.arange(24, 36).reshape((3, 4)), columns=['A', 'B', 'D', 'E'])
print(df2)
print(df3)

df7 = pd.concat([df2, df3], join='outer', ignore_index=True)    # 合并两个表， 缺少的部分填充NaN
print(df7)

#---------------------------
df8 = pd.concat([df2, df3], join='inner', ignore_index=True)    # 只会合并相同的列
print(df8)

# ------------------------
df9 = pd.concat([df2, df3], axis=0, join_axes=[df1.columns[:2]], ignore_index=True)  # 横向合并，index使用df1的index
print(df9)
