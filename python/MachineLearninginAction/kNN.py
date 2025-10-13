from numpy import *
import operator
import matplotlib.pyplot as plt
import numpy as np

"""
def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

group, labels = createDataSet()
print(group)
print(labels)

fig, ax = plt.subplots(figsize=(8,8))

ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)

colors = {'A': 'red', 'B': 'blue'}
for x, y in zip(group, labels):
    ax.scatter(x[0], x[1], c=colors[y])
    ax.text(x[0], x[1], y, fontsize=12, ha='right')

plt.show()
"""

# k-近邻算法
def classify0(inX, dataSet, labels, k):
    pass
