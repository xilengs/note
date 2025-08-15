from types import MethodType
# 定义了一个class，创建类的实例后，可以给实例绑定任何属性和方法
class Student(object):
    pass
# 给实例绑定属性
s = Student()
s.name = 'Michael'
print(s.name)
# 还可以尝试给实例绑定一个属性
def set_age(self, age):
    self.age = age
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)
# 为了给所有实例都绑定方法，还可以给class动态绑定方法：
def set_score(self, score):
    self.score = score
Student.set_score = set_score

# __slots__
# 限制实例的属性
class Students(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
s2 = Students()
s2.name = 'Michael'
s2.age = 25
# score不在定义内，不能绑定
# s2.score = 99
# __slots__仅对当前类的实例起作用，对子类不起作用