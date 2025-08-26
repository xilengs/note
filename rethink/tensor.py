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

# 在创建tensor时，Pytorch会根据你传入的数据，自动推断tensor的类型，也可以指定类型
t1 = torch.tensor((2,2), dtype=torch.float32)
print(t1)

# PtTorch里的数据类型，主要为：
# 整数型：torch.unit8、torch.int32、torch.int64。其中torch.int64为默认的整数类型
# 浮点型：torch.float16、torch.bfloat16、torch.float32、torch.float64。其中torch.float32为默认的浮点数据类型
# 布尔型 torch.bool

# bool类型tensor进行索引操作：
x = torch.tensor([1,2,3,4,5])
mask = x > 2
print(mask)

# 用布尔掩码选出大于2的值
filtered_x = x[mask]
print(filtered_x)

# 用布尔掩码选出大于2的值，并赋值为0
x[mask] = 0
print(x)

# 在创建tensor时，可以指定tensor的设备。默认在CPU/内存上。
# 创建一个GPU/显存上的tensor,通过参数device=cuda来指定
t_gpu = torch.tensor([1,2,3], device='cuda')

# 创建一个用指定值或者随机值填充的tensor，同时可以指定这个tensor的形状
shape = (2,3)
rand_tensor = torch.rand(shape) # 生成以从[0,1]均匀抽样的tensor
randn_tensor = torch.randn(shape)   # 生成一个从标准正态分布抽样的tensor
ones_tensor = torch.ones(shape)     # 生成一个值全为1的tensor
zeros_tensor = torch.zeros(shape)   # 生成一个值全为0的tensor
twos_tensor = torch.full(shape, 2)  # 生成一个值全为2的tensor

# tensor的属性：形状、元素的类型、设备
tensor = torch.rand(3,4)
print(f"shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

# 形状变换
x = torch.randn(4,4) # 生成一个4x4的随机矩阵
print(x)
x = x.reshape(2, 8)     # 通过reshape操作，可以将4x4的矩阵改变为2x8的矩阵
print(x)
# 通过reshape改变矩阵需要改变前后元素个数一致
# permute函数交换tensor的维度
x = torch.tensor([[1,2,3], [4,5,6]])
print(x)
x_reshape = x.reshape(3,2)
x_transpose = x.permute(1,0) # 交换第0个和第1个维度，行列互换
print('reshape:', x_reshape)
print('permute:', x_transpose)

# 对于二维tensor，可以调用tensor.t()方法进行转置操作。有时需要扩展tensor的维度，可以使用unsqueeze函数
x = torch.tensor([[1,2,3],[4,5,6]])
# 拓展第0维
x_0 = x.unsqueeze(0)
print(x_0.shape, x_0)
# 扩展第1维
x_1 = x.unsqueeze(1)
print(x_1.shape, x_1)
# 扩展第2维
x_2 = x.unsqueeze(2)
print(x_2.shape, x_2)

a = torch.ones((2,3))
b = torch.ones((2,3))
print('--------------------------------------')
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a @ b.t()) # 矩阵乘法

# 统计函数
# tensor.sum()求和，通过tensor.mean()求均值，通过tensor.std()求标准差，通过tensor.min()求最小值
print('--------------------------------')
t = torch.tensor([[1.0,3.0],[1.0,3.0],[1.0,3.0]])

mean = t.mean()
print("mean:", mean)
mean = t.mean(dim=0)
print('mean on dim 0:', mean)
mean = t.mean(dim=0, keepdim=True)
print("keepdim:", mean)
print('++++++++++++++++++++++++++++++++++++')
# tensor也支持索引和切片操作
x = torch.tensor([[1,2,3], [4,5,6]])
print(x[0,1])   # 访问第一行第二个元素
print(x[:,1])   # 访问第二列
print(x[1, :])  # 访问第二行
print(x[:,:2])  # 访问前两列

# 广播机制
t1 = torch.randn((3,2))
print(t1)
t2 = t1 + 1 # 广播机制，不需要创建tensor,也可以让t2全元素+1
print(t2)

print('=================================')
import time
# 确保GPU可用
device = torch.device('cuda' if torch.cuda.is_available() else 'CPU')
print(f'Using device: {device}')

# 生成随机矩阵
size = 10000
A_cpu = torch.rand(size, size)
B_cpu = torch.rand(size, size)

start_cpu = time.time()
C_cpu = torch.mm(A_cpu, B_cpu) # 矩阵乘法
end_cpu = time.time()
cpu_time = end_cpu - start_cpu

# 在GPU上计算
# 默认情况下，torch.rand会在CPU内存里生成随机矩阵，然后Pytorch自动把它搬到GPU上
# CPU->GPU内存拷贝非常耗时，所以可以直接在GPU上创建tensor
A_gpu = torch.rand(size, size, device='cuda')
B_gpu = torch.rand(size, size, device='cuda')

start_gpu = time.time()
C_gpu = torch.mm(A_gpu, B_gpu)
torch.cuda.synchronize()    # 确保GPU计算完成
end_gpu = time.time()
gpu_time = end_gpu - start_gpu

print(f"CPU time: {cpu_time:.6f} sec")
if torch.cuda.is_available():
    print(f"GPU time: {gpu_time:.6f} sec")
else:
    print('GPU not available, skipping GPU test.')