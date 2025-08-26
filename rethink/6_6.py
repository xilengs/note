# 使用PyTorch实现线性回归
import torch

# 确保cuda可用
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 生成数据
inputs = torch.rand(100, 3)
weights = torch.tensor([[1.1], [2.2], [3.3]]) # 预设权重
bias = torch.tensor(4.4)    # 预设bias
targets = inputs @ weights + bias + 0.1*torch.randn(100, 1) # 增加一些误差，模拟真实情况

# 初始化参数时直接放在cuda上，并启用梯度追踪
w = torch.rand((3,1), requires_grad=True, device=device)
b = torch.rand((1, ), requires_grad=True, device=device)

# train
inputs = inputs.to(device)
targets = targets.to(device)

# 设置超参数
epoch = 10000
lr = 0.003

for i in range(epoch):
    outputs = inputs @ w + b
    loss = torch.mean(torch.square(outputs - targets))
    print('loss: ', loss.item())

    loss.backward()

    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad

    # 清零梯度
    w.grad.zero_()
    b.grad.zero_()

print('训练后的权重w: ', w)
print('训练后的偏置 b:', b)