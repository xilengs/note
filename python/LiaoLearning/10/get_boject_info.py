import types
# 查询一个对象的类型
# 1.type()
# type()函数用于判断对象类型
class Animal(object):
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def run(self):
        print("Dog is running...")

class Cat(Animal):
    def run(self):
        print("Cat is running...")

class Husky(Dog):
    def run(self):
        print("Husky is fastly running...")

def fn():
    pass

def get_type():
    print(type(123))
    print(type('str'))
    print(type(None))
    # 如果一个变量指向函数或类也可以用type()判断
    print(type(abs))
    a = Animal()
    print((type(a)))
    # 使用type()判断类型
    print(type(123) == type(456))
    print(type(123) == int)
    print(type('abc') == str)
    print(type('abc') == type(123))
    # 判断对象是否是函数
    print(type(fn) == types.FunctionType)
    print(type(abs) == types.BuiltinFunctionType)
    print(type(lambda x : x) == types.LambdaType)
    print(type((x for x in range(10))) == types.GeneratorType)

# 2.isinstance
# 对于class继承关系来说，使用type()就很不方便了。要判断class的类型，可以使用isinstance()函数
def get_isinstance():
    a = Animal()
    dog = Dog()
    cat = Cat()
    husky = Husky()
    print(isinstance(husky, Husky))
    print(isinstance(husky, Dog))
    # 父类的父类也可以
    print(isinstance(husky, Animal))
    # 能用type()判断的基本类型isinstance也可以
    # 还可以判断一个变量是不是某些类型中的一种
    print(isinstance([1,2,3], (list, tuple)))

# 3.dir()
# 使用dir()函数，获得一个对象的所有的属性和方法，它返回一个包含字符串的list
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

def get_dir():
    print(dir('ABC'))
    # 类似__xxx__的属性和方法在python中都有特殊用途，比如__len__方法返回长度
    # 在python中如果你调用len()函数获得一个对象长度，实际上，在len()函数内部，他自动去调用该对象的__len()__方法
    ###
    # 温故而知新，print的内容中有'' 或者 "" 时，怎么办？
    ###
    print("len('ABC') = %s, 'ABC'.__len__() = %s"  % (len('ABC'), 'ABC'.__len__()))
    # 我们写自己的类，如果也想用len(myObj)的话，就可以写一个__len__()方法
    # 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr(),可以直接操作一个对象的状态
    obj = MyObject()
    # 有x属性吗
    print(hasattr(obj, 'x'))
    print(obj.x)
    print(hasattr(obj, 'y'))
    # 设置一个y属性
    print(setattr(obj, 'y', 19))
    print(hasattr(obj, 'y'))
    print(obj.y)
    # 如果试图获取不存在的属性，会抛出AttributeError的错误：
    # getattr(obj, 'z')
    # 可以传入一个default参数，如果属性不存在，就返回默认值：
    print(getattr(obj, 'z', 404))
    # 也可以获得对象的方法：
    print(hasattr(obj, 'power'))
    # 获得属性 'power'
    print(getattr(obj,'power'))
    # 获得属性 'power' 并赋值给fn
    fn = getattr(obj, 'power')
    print(fn())

get_type()
get_isinstance()
get_dir()