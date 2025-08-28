import pandas as pd

# 打印时显示所有列
pd.set_option('display.max_columns', None)

# 从csv文件读取数据
df = pd.read_csv(r'rethink/titanic/train.csv')
# 去除不要的列
df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])

# 去除Age缺失的样本
df = df.dropna(subset=['Age'])

# 对Sex和Embarked做独热编码
df = pd.get_dummies(df, columns=["Sex", "Embarked"], dtype=int)

print(df.head(10))

# Pytorch里的Dataset和DataLoader
# Dataset类提供对数据集的抽象，任何自定义数据集都需要继承torch.utils.data.Dataset,并实现两个方法：__len__和__getitem__(idx)
# 其中__len__需要返回整个数据集样本的个数，__getitem(idx)需要能根据样本的index返回具体的样本
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torch

class TitanicDataset(Dataset):
    def __init__(self, file_path):
        self.file_path = file_path
        self.mean = {
            "Pclass" : 2.236695,
            "Age": 29.699118,
            "SibSp": 0.512605,
            "Parch": 0.431373,
            "Fare": 34.694514,
            "Sex_female": 0.365546,
            "Sex_male": 0.634454,
            "Embarked_C": 0.182073,
            "Embarked_Q": 0.039216,
            "Embarked_S": 0.775910                     
        }

        self.std = {
            "Pclass": 0.838350,
            "Age": 14.526497,
            "SibSp": 0.929783,
            "Parch": 0.853289,
            "Fare": 52.918930,
            "Sex_female": 0.481921,
            "Sex_male": 0.481921,
            "Embarked_C": 0.386175,
            "Embarked_Q": 0.194244,
            "Embarked_S": 0.417274
        }

        self.data = self._load_data()
        self.feature_size = len(self.data.columns) - 1
    
    def _load_data(self):
        df = pd.read_csv(self.file_path)
        df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])
        df = df.dropna(subset=["Age"])
        df = pd.get_dummies(df, columns=["Sex", "Embarked"], dtype=int)

        # 进行数据的标准化
        base_features = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
        for i in range(len(base_features)):
            df[base_features[i]] = (df[base_features[i]] - self.mean[base_features[i]]) / self.std[base_features[i]]
        return df

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        features = self.data.drop(columns=["Survived"]).iloc[idx].values
        label = self.data["Survived"].iloc[idx]
        return torch.tensor(features, dtype=torch.float32), torch.tensor(label, dtype=torch.float32)
    
# 一般不需要自定义DataLoader，pytorch里默认实现的DataLoader就可以满足我们的使用
# 定义了如何批量读取数据的功能
# batchsize设置每次读取数据的大小
# shuffle参数设置是否对数据集进行打乱
dataset = TitanicDataset(r'c:/d/code/note/rethink/titanic/train.csv')
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
for inputs, labels in dataloader:
    print(inputs.shape, labels.shape)
    break