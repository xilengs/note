# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
# 实现一个可变参数的求和
# 求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
# 如果不需要立刻返回，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
# 当我们调用lazy_sum()时返回的并不是求和结果，而是求和函数：
f = lazy_sum(1,3,5,7,9)
# 再次调用返回计算结果
# a = f()
print(f())

# 返回的函数并没有立刻执行，直到调用f()才执行
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
# 调用均返回9
f1, f2, f3 = count()
print(f1(),f2(),f3())

# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值
def newcount():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        # f(i)立刻执行，因此i的当前值被传入f()
        fs.append(f(i))
    return fs

f4, f5, f6 = newcount()
print(f4(),f5(),f6())

# nonlocal
# 闭包：当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
# 使用闭包，返回函数不要引用任何循环变量，或者后续会发生变化的量
# 使用闭包，就是内层函数引用了外层函数的局部变量，如果只读外层变量的值，闭包函数调用一切正常
def inc():
    x = 0
    def fn():
        # 仅读取x的值：
        return x+1
    return fn

f = inc()
print(f())
print(f())

# 如果对外层变量赋值，由于python解释器会把x当作函数f()的局部变量，它会报错
# 原因是x作为局部变量没有初始化
# 加上nonlocal x声明x是外层函数变量
def non_inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

# 这里没法使用： non_f1, non_f2 = non_inc()
# 因为non_inc()返回的是单个函数，而不是函数队列
non_f = non_inc()
print(non_f())
print(non_f())

# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return x
    return counter

def test():
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')

test()