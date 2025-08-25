# Tensor是Pytorch里对多维数组的表示，用它来表示：
# 标量（0维）：单个数，比如torch.tensor(3.14)
# 向量（1维）：一列数，比如torch.tensor([1,2,3])
# 矩阵（2维）：行列数据，比如torch.tensor([[1,2], [3,4]])
# 高维张量（3维及以上）：高维数据，比如torch.tensor([[[1,2], [3,4]], [[5,6], [7,8]]])

# 创建Tensor
import torch
import numpy as np

# 1D Tensor
t1 = torch.tensor([1,2,3])
print(t1)

# 2D Tensor
t2 = torch.tensor([[1,2,3], [4,5,6]])
print(t2)

# 3D Tensor
t3 = torch.tensor([[[1,2], [3,4]], [[5,6], [7,8]]])
print(t3)

# 从Numpy 创建Tensor
arr = np.array([1,2,3])
print(arr)
t_np = torch.tensor(arr)
print(t_np)