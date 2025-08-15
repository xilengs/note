import os   #导入os模块
# 列表生成式即list Comprehensions，是python内置的非常简单却强大的可以用来创建list的生成式
# 生成list[1,2,3,4,5,6,7,8,9,10]
l = list(range(1,11))
print(l)

# 生成[1x1,2x2,3x3,4x4,5x5,6x6,7x7,8x8,9x9,10x10]
# 使用for循环
L = []
for x in range(1, 11):
    L.append(x*x)
print(L)
# 使用列表生成式
L = []
L = [x * x for x in range(1, 11)]
print(L)
# for循环后面还可以加上if判断
#L = []
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)
# 还可以使用两层循环，可以生成全排列
s = [m + n for m in 'ABC' for n in 'XYZ']
print(s)
# 列出当前目录下的所有文件和目录名
print(d for d in os.listdir('.'))

#列表生成式也可以使用两个变量来生成list
d = {'x':'A', 'y':'B', 'z':'C'}
ds = [k + '=' + v for k,v in d.items()]
print(ds)
# 把一个list中所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
L_lower = [d.lower() for d in L]
print(L_lower)

# 在列表生成式中使用if...else
# 前一个不能加else，后一个可以
# for前是一个表达式，必须有结果
print([x for x in range(1,11) if x % 2 == 0])
print([x if x % 2 == 0 else -x for x in range(1,11)])

# 练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() if isinstance(s, str) else s for s in L1]
print(L2)