# 定制类
# __str__
# 返回自定义字符串
from tkinter.font import names

from sympy.solvers.diophantine.diophantine import length


class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Michael'))

class Students(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

print(Students('Anna'))

# 但是直接在命令行输入s，还是会返回上面一种输出
# >>> s
# <__main__.Student object at 0x000001EC2D0774D0>
# 是因为直接显示变量调用的不是__str__()，而是__repr__()
# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
# 解决办法是再定义一个__repr__()
# 通常__str__()和__repr__()代码是一样的，所以可以这样像上面那样写


# __iter__
# 如果一个类想被用于for...in循环，就必须实现__iter__()方法，该方法返回一个迭代对象
# 然后python的for循环就会不断调用该迭代对象的__next__()方法拿到下一个值，直到遇到StopIteration错误时退出循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是把它当作list来用还是不行
# >>> fib()[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'Fib' object does not support indexing
# 要像list一样可以用下标取出元素，需要实现__getitem__()方法
class Fib2(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b , a+b
        return a
# 现在可以用下标访问Fib2()了
f = Fib2()
# print(f[0],f[1],f[2],f[3],f[10],f[100])

# 实现切片功能，需要判断一下输入的参数是int还是切片对象slice
class Fib3(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a,b = 1,1
            for x in range(item):
                a, b = b, a+b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start in None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L
# 如果把对象堪称dict,__getitem__()的参数也可能是一个作为key的object，例如str
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值
# __delitem__()用于删除某个元素

# __getattr__()
# 正常情况下，调用类的属性或方法，如果这个属性或方法不存在，就会报错
# __getattr__()可以动态的返回一个属性
class Person(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == 'score':
            return 99

# 当调用不存在的属性时(score)，python会从__getattr__()来尝试获得属性，这样就可以返回score的值了
p = Person('Jack')
print(p.name)
print(p.score)

# 返回函数也可以
class Persons(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == 'age':
            return lambda : 25
# 只是调用方式要改变
p2 = Persons('Mike')
print(p2.age())
# 只有在找不到属性或者函数时，才会调用__getattr__
# 任意调用如p2.abc都会返回None,因为__getattr__()默认返回None
# 要让class只响应特定几个属性，按照约定，抛出AttributeError错误
# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段
class MyStudent(object):
    def __getattr__(self, item):
        if item == 'age':
            return lambda : 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

ms = MyStudent()
# ms.change()

# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()的形式来调用
# 除此之外，还可以直接在实例本身上调用
# 任何类只要定义一个__call__()方法，就可以直接对实例进行调用
class StudentA(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = StudentA('Michael')
s()
# 这样就可以像使用函数那样使用实例，实例是callable对象
print(callable(StudentA('Jack')))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))