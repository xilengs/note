# 匿名函数
l = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda x: x*x, l)))
# 上面map()使用的匿名函数就是
def f(x):
    return x*x
# 匿名函数只能有一个表达式，不用写return，返回值就是该表达式的结果
# 可以把匿名函数赋给一个变量，用变量来调用，这样和直接写函数也没啥区别了
f1 = lambda x : x*x
# 同样也可以把匿名函数作为返回值返回
def build(x,y):
    return lambda : x*x + y*y

# 练习
# 用匿名函数改造下面代码
def is_odd(n):
    return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))
L = list(filter(lambda n: n%2 == 1, range(1,20)))

print(L)
