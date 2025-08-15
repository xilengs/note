#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# 第一行注释可以让这个python文件直接在Unix/Linux/Mac上运行
# 第二行注释表示.py文件本身使用标准utf-8编码

""" a test module """
# 任何模块代码的第一个字符串被视为模块的文档注释

# 作者姓名
__author__ = 'xilengs'

# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一次参数永远是该.py文件的名称
import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 作用域
# 在一个模块中，我们可能定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用
# 在python中，是通过_前缀来实现的
# 正常的函数和变量名时公开的，可以被直接引用
# 类似__xxx__这样的变量是特殊变量，可以被直接引用
# 类似_xxx和__xxx这样的函数或变量就是非公开的，不应该被直接引用
# 但是python并没有一种方法可以完全限制访问private函数或变量，但是从编程习惯上不应该引用private函数或变量
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

if __name__=='__main__':
    test()