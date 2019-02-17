import numpy as np
import pandas as pd

data = pd.read_excel('HOUSE.xls')
print(data)
print(data[data['Global_intensity'] > 15])
data1 = data[data['Global_intensity'] > 15]
print(data1['Voltage'].value_counts())
print(data1['Voltage'].mean())
