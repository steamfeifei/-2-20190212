import numpy as np
import pandas as pd

left = pd.DataFrame({
                     'key1':['KO', 'K0', 'K2', 'K3'],
                     'key2':['KO', 'K1', 'K2', 'K3'],
                     'A':['AO', 'A1', 'A2', 'A3'],
                     'B':['BO', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1':['KO', 'K0', 'K0', 'K0'],
                     'key2':['KO', 'K1', 'K2', 'K3'],
                      'C':['C0', 'C1', 'C2', 'C3'],
                      'D':['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)

# pd1 = pd.merge(left, right, on='key')       # 按照相同的列key合并
# print(pd1)

pd2 = pd.merge(left, right, on=['key1', 'key2'], how='inner')
print(pd2)
pd3 = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print(pd3)
pd4 = pd.merge(left, right, on=['key1', 'key2'], how='left')
print(pd4)
pd5 = pd.merge(left, right, on=['key1', 'key2'], how='right')
print(pd5)


pd6 = pd.merge(left, right, on=['key1', 'key2'], how='right', indicator=True)   # 显示merge信息
pd6 = pd.merge(left, right, on=['key1', 'key2'], how='right', indicator='indicatior_column')   # 显示merge信息
print(pd6)
#   key1 key2    A    B   C   D      _merge
# 0   KO   KO   AO   BO  C0  D0        both
# 1   K0   K1   A1   B1  C1  D1        both
# 2   K0   K2  NaN  NaN  C2  D2  right_only
# 3   K0   K3  NaN  NaN  C3  D3  right_only

#   key1 key2    A    B   C   D indicatior_column
# 0   KO   KO   AO   BO  C0  D0              both
# 1   K0   K1   A1   B1  C1  D1              both
# 2   K0   K2  NaN  NaN  C2  D2        right_only
# 3   K0   K3  NaN  NaN  C3  D3        right_only


pd7 = pd.merge(left, right, left_index=True, right_index=True, how='outer', suffixes=['_left', '_right'])   # 合并时相同的列会自动加上下划线区分
print(pd7)
