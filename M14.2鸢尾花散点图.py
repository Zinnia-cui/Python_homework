import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取 iris 数据集
df = pd.read_csv("iris.csv")

# 筛选出品种为 setosa 的鸢尾花数据
setosa_data = df[df['Species'] == 'setosa']
# 筛选出品种为 versicolor 的鸢尾花数据
versicolor_data=df[df['Species'] == 'versicolor']
# 筛选出品种为 virginica的鸢尾花数据
virginica_data=df[df['Species'] == 'virginica']

#散点可视化
plt.scatter(setosa_data.iloc[:, 1], setosa_data.iloc[:, 2], marker='o', c='r', label='setosa')
plt.scatter(versicolor_data.iloc[:, 1], versicolor_data.iloc[:, 2], marker='s', c='b', label='versicolor')

plt.scatter(virginica_data.iloc[:, 1], virginica_data.iloc[:, 2], marker='^', c='g', label='virginica')
plt.xlabel('Sepal Length', fontsize=14)
plt.ylabel('Sepal Width', fontsize=14)
plt.savefig('f.eps')
plt.legend(loc='upper right')
