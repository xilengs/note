import pandas as pd

df = pd.read_csv('rethink/titanic/train.csv')

train_set = df.iloc[:800]
val_set = df.iloc[800:]

# 保存结果
train_set.to_csv("rethink/titanic/train_set.csv", index = False)
val_set.to_csv('rethink/titanic/val_set.csv', index = False)