# L1 和 L2 正则化

# 什么是正则化
# 用来限制模型复杂度、防止过拟合的方法

# L1 正则化
# 在loss中加入模型所有参数的绝对值之和作为惩罚项
# 效果: 会尽可能让参数变小来降低Loss，直到让某些参数为0
# 容易导致过拟合，模型参数变稀疏

# L2 正则化
# 在loss中加入模型所有参数的平方和作为惩罚项
# 会让模型参数变小，但不会变为0
# 在PyTorch里增加L2正则化
import torch

l2_norm = 0.0
for param in model.parameters():
    l2_norm += param.pow(2).sum()
loss = criterion(outputs, labels) + 1e-4 * l2_norm