# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承
# 新的class称之为子类(Subclass),而被继承的class称之为基类、父类或超类(Base class、Super class)
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Dog is eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Cat is eating meat...')

# Dog继承自Animal类，Dog类也属于Animal类
dog = Dog()
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
# 所以在一个继承关系中，如果一个实例的数据类型是某个子类，那么它的数据类型也可以被看作是父类，但是反过来就不行

def run_twice(animal:Animal):
    animal.run()
    animal.run()
# 传入animal实例
animal = Animal()
run_twice(animal)
# 也可以传入子类实例
run_twice(dog)
# 新增一个子类
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

tortoise = Tortoise()
run_twice(tortoise)
# 新增子类也可以直接传入运行
# 开闭原则：
# 对扩展开放：允许新增子类
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数

# 静态语言 vs 动态语言
# 对于静态语言（例如Java)来说，如果需要传入Animal类型，则传入的对象必须是Animal类或它的子类，否则无法运行run_twice()函数
# 但对于python这样的动态语言，只需要保证传入的对象有一个run()方法就可以了
# 所以上述函数其实有run()方法就可以了，不需要一定是Animal的类