# 枚举
from enum import Enum, unique

Month = Enum('Month', ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
for name, member in Month.__members__.items():
    print(name, '=>', member,',',member.value)
# value属性是自动赋给成员的int常量，默认从1开始计数

# 用类的形式定义枚举
# @unique装饰器用于检查是否有重复值
@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

for color, member in Color.__members__.items():
    print(color, '=>', member, ',' ,member.value)

# 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串
print('----------------------------------------')
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        if not isinstance(gender, Gender):
            raise ValueError('gender should be Enum!')
        self.name = name
        self.gender = gender

def test():
    bart = Student('Bart', Gender.Male)
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')

test()
print('----------------------------------------')