# 调试
# 最简单的方法，就是print()把有可能有问题的变量打印出来看看

# 断言(assert)
def foo(s):
    n = int(s)
    # assert n != 0,否则抛出异常'no is zero!'
    assert n != 0, 'n is zero!'

def main():
    foo('0')

# main()

# 启动python解释器时，可以用-o参数关闭assert
# 大写o
# $ python -O debug.py

# logging
# logging不会抛出错误，而且可以输出到文件
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
# print(10 / n)

# pdb
# 启动python调试器pdb, 让程序以单步方式运行，可以随时查看运行状态
# python -m pdb err.py  # 启动
# 输入命令 l 查看代码
# 输入命令n可以单步执行代码
# 任何时候都可以输入命令p查看变量
# 输入命令q结束调试，退出程序

# pdb.set_trace()
import  pdb
# 在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
# $ python err.py # 直接运行代码，程序会在断点处暂停并进入pdb调试环境