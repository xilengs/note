# 高阶函数(Higher-order function)
# 函数本身也可以赋值给变量
def functionPara():
    # 以abs()函数为例
    # 把函数结果赋给x
    x = abs(-10)
    print(x)
    # 把函数本身赋给f
    f = abs
    print(f)
    # 可以用f调用abs()函数
    y = f(-1)
    print(y)
    # 函数名其实就是指向函数的变量
    # 如果把函数名指向其他对象，就无法通过原先的函数名调用原先的函数了
    '''
    abs = 10
    z = abs(-10)
    print(z)
    '''


functionPara()


# 传入函数参数
def add(x,y,f):
    return f(x) + f(y)

print(add(3,-3,abs))
# 编写高阶函数就是让函数的参数能够接收别的函数