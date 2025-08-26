# PyTorch自动求梯度
import torch

x = torch.tensor(1.0, requires_grad=True)
y = torch.tensor(1.0, requires_grad=True)
v = 3*x + 4*y
u = torch.square(v)
z = torch.log(u)

z.backward()    # 反向传播求梯度

print(f"x grad: {x.grad}")
print(f"y grad: {y.grad}")