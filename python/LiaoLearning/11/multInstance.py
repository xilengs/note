# 多重继承
class Animal(object):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        ptint('Flying...')

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 继承了Mammal类 和 Runnable类
class Dog(Mammal, Runnable):
    pass

# 继承了 Mammal类 和 Flyable类
class Bat(Mammal, Flyable):
    pass

# 通过多重继承，一个子类可以同时得到多个父类的所有功能

# MixIn
# 在设计类的继承关系时，通常主线都是单一继承下来的，如Dog继承自Mammal类，Mammal继承自Animal类
# 但是如果要"混入"额外的功能，通过多重设计可以实现，比如让Dog继承Mammal类外再继承Runnable类
# 这种设计通常称之为 MixIn

