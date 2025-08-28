import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
inputs = torch.tensor([[2,1000], [3,2000], [2,500], [1,800], [4,3000]], dtype=torch.float, device=device)
labels = torch.tensor([[19], [31], [14], [15], [43]], dtype=torch.float, device=device)

mean = inputs.mean(dim=0)
std = inputs.std(dim=0)

# 对feature进行归一化处理
def train1(): 
    # 进行归一化处理
    # 如果数据量大，要怎得到这个[4, 3000]这个值
    inputs = inputs / torch.tensor([4, 3000], device=device)

    w = torch.ones(2, 1, requires_grad=True, device=device)
    b = torch.ones(1, requires_grad=True, device=device)

    epoch = 10000
    Ir = 0.01

    for i in range(epoch):
        outputs = inputs @ w + b
        loss = torch.mean(torch.square(outputs - labels))
        print('loss', loss.item())
        # 会把本次反向传播计算得到的梯度累加到w.grad和b.grad上，而不是覆盖掉原来的值
        loss.backward()
        print('w.grad', w.grad.tolist())
        with torch.no_grad():
            w -= w.grad * Ir
            b -= b.grad * Ir

        w.grad.zero_()
        b.grad.zero_()

# 对特征进行标准化
def train2():
    # 计算特征的均值和标准差
    # mean = inputs.mean(dim=0)
    # std = inputs.std(dim=0)
    # 对特征进行标准化
    inputs_norm = (inputs-mean)/std

    w = torch.ones(2, 1, requires_grad=True, device=device)
    b = torch.ones(1, requires_grad=True, device=device)

    epoch = 1000
    Ir = 0.01

    for i in range(epoch):
        outputs = inputs_norm @ w + b
        loss = torch.mean(torch.square(outputs - labels))
        print('loss', loss.item())
        loss.backward()
        print('w.grad', w.grad.tolist())
        with torch.no_grad():
            w -= w.grad * Ir
            b -= b.grad * Ir
        
        w.grad.zero_()
        b.grad.zero_()
    
    return w, b

if __name__ == '__main__':
    # 对feature进行归一化，固定值
    # train1()
    w, b = train2()
    # 训练时对数据做了归一化，那么一定要记录做归一化时的参数，在数据预测时，首先对feature进行同样的归一化，然后再带入模型
    new_input = torch.tensor([[3,2500]], dtype=torch.float, device=device)
    new_input = (new_input-mean)/std
    # 预测
    predict = new_input @ w + b
    print('predict:', predict.tolist()[0][0])