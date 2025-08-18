# 使用元类
# 动态语言和静态语言最大的不同就是函数和类的定义，不是编译时定义，而是运行时动态创建的
from hello import Hello

h = Hello()
h.hello()
# Hello 是一个class，他的类型就是type
print(type(Hello))
# <class 'type'>
print(type(h))
# <class 'hello.Hello'>

# type()除了可以查看一个类型或变量的类型，还可以创建出新的类型
# 通过type()创建MyHello类，而不需要通过 class MyHello(object)...创建
def fn(self, name='new world'):
    print('Hello, %s' % name)

# type(class的名称, (继承的父类集合,), class的方法名称与函数绑定)
# 实际和class定义一样，不过更抽象
# 实际python解释器在遇到class定义时，将其转化为type()函数进行创建
# 所有使用type()创建类可能更快？
MyHello = type('MyHello', (object,), dict(hello=fn)) # 创建MyHello class
h2 = MyHello()
h2.hello()
print(type(Hello))
print(type(h2))

# metaclass 元类
# metaclass也可以控制类的创建行为
# 先定义metaclass,再定义类，在定义实例
# metaclass允许你创建类或者修改类
# 基本用不到
# metaclass是类的模板，所以必须从'type'类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 根据ListMetaclass来定制类
class MyList(list, metaclass=ListMetaclass):
    pass
