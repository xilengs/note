# 如果不想外部函数可以访问内部函数属性，可以在属性名称前加两个下划线__
# 在python中，实例的变量名如果以__开头，就变成了私有变量，只有内部可以访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

# 获取属性
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 修改属性
    # 可以对参数进行检查，避免传入无效参数
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

# 双下划线的实例变量也可以访问，不能直接通过__name访问是因为python解释器对外把__name变量改成了_Student_name
# 所以，仍然可以通过_Student__name来访问__name变量

# 练习
# 把下面Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查有效性
print('------------------------------------------')
'''
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
'''
class Students(object):
    def __init__(self, name, gender):
        self.__name = name
        if gender in ('male', 'female'):
            self.__gender = gender
        else:
            raise ValueError('ErrorGender')

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('ErrorGender')

def test():
    bart = Students('Bart', 'male')
    if bart.get_gender() != 'male':
        print('测试失败!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败!')
        else:
            print('测试成功!')

test()
print('------------------------------------------')