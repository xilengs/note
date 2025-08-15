from collections.abc import Iterable
# 迭代：使用for循环来遍历list或者tuple，这种遍历称之为迭代（iteration)
# python的迭代无论有没有下标都可以迭代，只要是可迭代对象
d = {'a':1, 'b':2,'c':3} # 字典dict
for key in d:   #遍历key
    print(key)
for value in d.values():    #遍历value
    print(value)
for key,value in d.items():     #同时遍历key和value
    print(key, value)

# 字符串也是可迭代对象
ch = "intersting"
for letter in ch:
    print(letter)

# 如何判断一个字符串是不是可迭代对象
# 方法是通过collections.abc模块的Iterable类型判断
is_iterable = isinstance('abc', Iterable)
print(is_iterable)
is_iterable = isinstance([1,2,3], Iterable)
print(is_iterable)
is_iterable = isinstance(123, Iterable)
print(is_iterable)
# isinstance()用于判断一个对象是否是某个类或类型的实例
# isinstance(object, classinfo)
# object : 要判断的对象  classinfo : 类、类型，或者由它们组成的元组
# 返回值 True/False
print(isinstance("hello", str)) # 判断是否是字符串
print(isinstance(123, int)) # 判断时候是整数
print(isinstance(3.14, (int, float))) # 判断是否是多类型之一

# type(obj)h返回obj的类型对象，等价于obj.__class————
# 于isinstance()的用处类似，但isinstance()会考虑继承关系，而type()只判断类型是否完全一致
x = 3
print(type(x))
print(type(x) == int)   #判断x是不是int型

# 动态创建一个类 type(name, bases, dict) ————动态创建一个类，等同于用class语句定义类，但在运行时生成
# 参数: name: 类名 bases: 基本元组(例如(object,)) dict: 属性与方法的字典
def __init__(self, x):
    self.x = x

def move(self, dx):
    self.x += dx

Point = type('Point', (object,), {'__init__':__init__,'move':move})

p = Point(5)
p.move(3)
print(p.x)

# 对list实现下标循环(使用enumerate)
# enumerate()函数可以把一个list变成索引——元素对
for i, value in enumerate(['A','B','C']):
    print(i, value)

# 练习
# 使用迭代器查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if L == []:
        return None, None
    elif len(L) == 1:
        return L[0], L[0]

    min = max = L[0]
    for i in L:
        if i < min:
            min = i
        elif i > max:
            max = i
    return min, max

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')