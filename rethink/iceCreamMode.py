X = [[10, 3], [20, 3], [25, 3], [28, 2.5], [30, 2], [35, 2.5], [40, 2.5]]
Y = [60, 85, 100, 120, 140, 145, 163]
# 初始化参数
w = [94.6, 3.06, -22.9] # w0, w1, w2
Ir = 0.001         # 学习率
num_iterations = 1000000  # 迭代次数

# 梯度下降
for i in range(num_iterations):
    y_pred = [w[0] + w[1] * x[0] + w[2] * x[1] for x in X]
    loss = sum((y_pred[j] - Y[j]) ** 2 for j in range(len(Y))) / len(Y)
    # 计算梯度
    grad_w0 = 2 * sum(y_pred[j] - Y[j] for j in range(len(Y))) / len(Y)
    grad_w1 = 2 * sum((y_pred[j] - Y[j]) * X[j][0] for j in range(len(Y))) / len(Y)
    grad_w2 = 2 * sum((y_pred[j] - Y[j]) * X[j][1] for j in range(len(Y))) / len(Y)

    # 更新参数
    w[0] -= Ir * grad_w0
    w[1] -= Ir * grad_w1
    w[2] -= Ir * grad_w2
    # 打印损失
    if i % 100 == 0:
        print(f"Inertion {i}: Loss = {loss}")
    
# 输出最终参数
print(f"Final parameters: w0 = {w[0]}, w1 = {w[1]}, w2 = {w[2]}")
