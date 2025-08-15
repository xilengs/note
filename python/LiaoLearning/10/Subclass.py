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
