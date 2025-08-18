# try
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
# 当我们认为某些代码可能会出错时，就用try来运行代码，如果执行出错，则后续代码不会继续执行
# 而是跳转到错误代码处理，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块
# finally如果有一定会被执行
try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# 可以有多个except来捕获不同类型的错误
try:
    print("try...")
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

# 如果没有错误发生，可以在except语句块后面加一个else，没有错误发生会自动执行else语句：
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# python的错误也是class，所有的错误类型都继承自BaseException
# 在使用except时要注意，它不但会捕获该类那个的错误，还会把子类也全捕获
# 第二个except永远也捕获不到错误，因为UnicodeError是ValueError的子类
try:
    pass
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')

# try...except...捕获错误可以跨越多层调用
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()

# 调用栈
# 如果错误没有被捕获，它会一直往上抛，最后被python解释器捕获，打印一个错误信息，然后程序退出


# 记录错误
# python内置的logging模块可以非常容易地记录错误信息：
# 但是程序会先运行完毕，再抛出错误信息
import logging
def main2():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
# main2()
print('END')

# 练习
# 运行下面代码，根据异常信息进行分析，定位错误源头，并修复
print('----------------------------------')
from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    # r = calc('99 + 88 + 7.6')
    r = calc('99 + 88 + 76')
    # 输入非int参数
    # print('99 + 88 + 7.6 =', r)
    print('99 + 88 + 76 =', r)

main()
print('----------------------------------')