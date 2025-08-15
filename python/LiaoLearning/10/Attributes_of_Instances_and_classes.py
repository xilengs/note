# 由于python是动态语言，根据类创建的实例可以任意绑定属性
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    name = 'Student'
    def __init__(self, name=None):
        if name:
            self.name = name

s = Student('Bob')
# 给实例绑定的属性，Student类没有score这个变量
s.score = 90
# 给类绑定属性，直接在类内定义变量即可，这种属性时类属性，归Student类所有
s2 = Student()
print(s.name)
print(s2.name)
# 实例的属性优先级高于类属性，如果对实例重定义属性，依实例的为准
s2.name = 'NewName'
print(s2.name)
print(Student.name)
# 删除实例的name属性
del s2.name
print(s2.name)

# 练习
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
print('---------------------------------------')
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

def test():
    if Student.count != 0:
        print('测试失败!')
    else:
        bart = Student('Bart')
        if Student.count != 1:
            print('测试失败!')
        else:
            lisa = Student('Bart')
            if Student.count != 2:
                print('测试失败!')
            else:
                print('Students:', Student.count)
                print('测试通过!')

test()
print('---------------------------------------')