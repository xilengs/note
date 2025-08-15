from sympy.stats import StudentT

## 面向对象编程
面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把**对象**作为程序的基本单元，一个对象包含了数据和操作数据的函数。

面向过程的设计把计算机程序视为**一系列的命令集合**，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是**一系列消息在各个对象之间的传递**。

面向过程：
```python
std1 = {'name':'Michael', 'score':98}
srd2 = {'name':'Bob', 'score':81}

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
```

面向对象：
```python
class Students(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Students('Bart Simpson', 59)
lisa = Students('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
```

给对象发消息实际上就是调用对象对应的关联函数，称之为**对象的方法(Method)**。
