# 生成器 generator 一边循环一边计算
# 创建list
from sympy import resultant, print_tree

L = [x * x for x in range(10)]
# 创建generator
g = (x * x for x in range(10))
print(L,g)
# list和generator的区别仅在于最外层的[]和()
# 通过next()函数获得generator的下一个返回值
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# 每次调用next(g)，计算出g的下一个元素的值，直到计算到最后一个元素
# generator中没有更多元素时，抛出StopIteration的错误
# 使用for循环调用generator
g = (x * x for x in range(10))
for n in g:
    print(n)

# 斐波那契数列
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b, a+b
        n += 1
    return 'done'
# fib(6)
# 使用generator方式
def fib2(max):
    n,a,b = 0,0,1
    while n < max:
        yield b     #yield关键字，则函数为generator函数
        # print(b)
        a,b = b,a+b
        n += 1
    return 'done'
# 调用generator函数将返回一个generator
f = fib2(6)
for i in f:
    print(i)
# 在generator函数中，return只能用来结束generator
# 想要获得generator中的返回值，可以从generator结束迭代后抛出的异常中获得
# 异常对象的,value属性就是return后的返回值
g = fib2(8)
try:
    while True:
        print(next(g))
except StopIteration as e:
    print("Generator 返回值是：", e.value)

# 练习
# 用generator输出杨辉三角
def triangles():
    l = [1]
    left = 0
    while True:
        yield l
        l = [x+y for x,y in zip([0]+l, l+[0])]

def test():
    n = 0
    result = []
    for t in triangles():
        result.append(t)
        n += 1
        if n == 10:
            break
    for t in result:
        print(t)

    if result == [
        [1],
        [1,1],
        [1,2,1],
        [1,3,3,1],
        [1,4,6,4,1],
        [1,5,10,10,5,1],
        [1,6,15,20,15,6,1],
        [1,7,21,35,35,21,7,1],
        [1,8,28,56,70,56,28,8,1],
        [1,9,36,84,126,126,84,36,9,1]
    ]:
        print('测试通过')
    else:
        print('测试不通过')

test()