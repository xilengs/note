import torch
# clamp
# clamp是PyTorch里常用的一个张量操作，用来限制数值的范围
# 超出最大值或最小值的值会被截断成最大值或者最小值
# torch.clamp(input, min=None, max=None)
x = torch.tensor([-2.0, -0.5, 0.3, 2.5, 5.0])
y = torch.clamp(x, min=0.0, max=3.0)
print('x原张量: ', x)
print(f'经过clamp处理的x张量: {y}')

# torch.max()
# torch.max(input, dim, keepdim=False, out=None)->(Tensor, LongTensor)
# 1.取整个张量的最大值(标量)
x = torch.tensor([[2.,1.,0.1], [3.,5.,4.]])
print(x.max())   # torch.max(x)
# 2.沿某个维度取最大值(返回值和索引)
vals, idxs = x.max(dim=1, keepdim=True)
print(f"vals: {vals}, idxs: {idxs}")
# dim=1 表示按行找每一行的最大值; dim=0 表示按列找每一列的最大值
# keepdim=True会保留被归约的那个维度（长度为1）方便广播
x_exp = torch.max(x-vals)
print(x_exp)
# 3.逐元素最大值（两个张量或与标量）
a = torch.tensor([1., 4., 3.])
b = torch.tensor([2., 2., 5.])
a_b = torch.max(a, b)
a_2 = torch.max(a, torch.tensor(2.0))
print(f"a: {a}, b: {b}")
print(f"torch.max(a, b): {a_b}")
print(f"torch.max(a, torch.tensor(2.0)): {a_2}")

