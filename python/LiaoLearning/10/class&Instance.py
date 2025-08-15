# 类(class)和实例(Instance)
# 实例是根据类创建出来的一个个具体的对象，每个对象都拥有相同的方法，单各自的数据可能不同
# (object)表示该类是从那个类继承下来的，通常如果没有合适的继承类，就是用object类，这是所有类最终都会继承的类
class Students(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 创建实例
bart = Students('Bart Simpson', 98)
# 和普通的函数不同，类中定义的函数第一个参数永远是实例变量self，并且调用的时候不用传递该参数

# 数据封装
# 面向对象编程的一个重要特点就是数据封装
# 上面的Students类每个实例就拥有各自的name和score这些数据，可以通过函数来访问这些数据
# 在Students的内部定义访问数据的函数，就没必要从外面的函数访问了
# 这些封装数据的函数是和Students类本身关联起来的，我们称之为类的方法
# 封装的另一个好处就是可以给Students类增加新的方法：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'