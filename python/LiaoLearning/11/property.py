# @property
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改
# 为了限制score的范围，通过set_score()设置成绩，通过get_score()来获取成绩
class Student(object):
    def __init__(self, value=0):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

s = Student(60)
print(s.get_score())
s.set_score(99)
print(s.get_score())
# s.set_score(999)
print(s.get_score())

# 使用装饰器给函数动态加上检查and访问功能
# 把一个getter方法变成属性，只需要加上@property就可以了
# @property又创建了另一个装饰器@score.setter,负责把另一个setter方法变成属性赋值
class Students(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

# 通过上述操作，就得到了可控的属性赋值
s1 = Students()
s.score = 60 # 实际转化为s.score(60)
print(s.score) # 实际转化为s.score()

# 使用@property定义只读属性(只定义getter方法，不定义setter方法)
# birth为可读可写属性，age为只读属性
class NewStudent(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, int):
            raise ValueError('birth should be integer!')
        if value < 1900 or value > 2025:
            raise ValueError('birth too small or too big!')
        self._birth = value

    @property
    def age(self):
        return 2025 - self._birth

# 注意属性的方法名不要和实例变量重名
# 重名导致无限递归调用，导致栈溢出
"""
class Student(object):
    @property
    def birth(self):
        return self.birth
"""

# 练习
# 请利用@property给一个Screen对象加上width喝height属性，以及一个只读属性resolution:
"""
class Screen(object):
    pass
"""
class Screen(object):
    def __init__(self, w=0, h=0, r=786432):
        if not isinstance(w, (float, int)) or not isinstance(h, (float, int)):
            raise ValueError('width and height should be int or float!')
        if w < 0 or h < 0:
            raise ValueError('width and height should be positive!')
        self._width = w
        self._height = h
        self._resolution = r

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError('width should be int or float!')
        if value < 0:
            raise ValueError('width should be positive!')
        self._width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError('height should be int or float!')
        if value < 0:
            raise ValueError('height should be positive!')
        self._height = value

    @property
    def resolution(self):
        return self._resolution

def test():
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')

test()