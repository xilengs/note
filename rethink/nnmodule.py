# nn.Module是pytorch里的核心组件，在pytorch里所有模型或者模型内的模块都是基于nn.module构建的
# nn.Module的好处
# 1.模块化构建，对于复杂的网络，可以将它划分为多个子模块进行构建，然后将他们组合成一个复杂的模型
# 2.自动管理参数：nn.Module会自动追踪模块内所有的参数，可以通过模块的parameters()或者named_parameters()进行查看
# 3.统一的forward方法，所有继承自nn.module的类必须实现一个forward方法，这样各个模块之间根据组合关系对数据进行前向处理。
# 4.统一的设备管理: 利用nn.Module提供的.to(device)方法，可以方便的将整个模型迁移到GPU或CPU
# 5.提供了模型的保存和加载的方法
# 6. 定义了train和eval状态，有的模块在训练时和预测时前向传播实现是不同的，可以通过model.train()和model.eval()切换
# 要自定义一个模型，需要继承nn.module,然后实现两个方法，一个是__init__,一个是forward
import torch.nn as nn
import torch
class LogisticPegressionModel(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.linear = nn.Linear(input_dim, 1)

    def forward(self, x):
        return torch.sigmoid(self.linear(x))