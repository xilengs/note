# 单元测试
# 把各种不同的测试用例放到一个测试模块里，就是一个完整的单元测试
# 编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问
# mydict.py
# >>> d = Dict(a=1, b=2)
# >>> d['a']
# 1
# >>> d.a
# 1
# 单元测试
# mydict_test.py
# 运行单元测试
# python my_dict_test.py
# Ran 5 tests in 0.013s
# OK
# 可以通过module.class.method来运行单个测试方法，反复多次测试同一方法
# python -m unittest mydict_test.TestDict.test_attr
# Ran 1 test in 0.000s
#
# OK
# 其中module是文件名mydict_test(不含.py),class是测试类TestDict,method是指定的测试方法名test_attr
# 如果希望执行test_attr()和test_attrerror()两个测试方法，可以传入-k参数，用attr来匹配
# python -m unittest mydict_test -k attr -v
# -v 参数能打印出具体执行的测试方法
# -k attr参数筛选出了包含attr的测试方法

# setUp 和 tearDown
# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法分别在每调用一个测试方法的前后分别执行

# 练习
# 对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过
# 错误：get_grade()分层输出不对，没有score超出范围时抛出异常
import unittest

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

#     def get_grade(self):
#         if self.score >= 60:
#             return 'B'
#         if self.score >= 80:
#             return 'A'
#         return 'C'

    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError
        if self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 0)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()