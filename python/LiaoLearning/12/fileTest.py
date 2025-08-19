# 自动执行写在注释中的代码
def abs(n):
    """
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    """
    return n if n > 0 else (-n)
# python内置的"文档测试"(doctest)模块可以直接提取注释中的代码并执行测试
# doctest严格按照python交互式命令行的输入和输出判断测试结果是否正确。只有测试异常时，可以用...表示中间一大段烦人的输出
# 使用doctest测试上次编写的Dict类

# 练习
# 对fact(n)编写doctest并执行：
print('---------------------------------------------')
def fact(n):
    """
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: -1
    """
    if n < 1:
        raise ValueError
    if n == 1:
        return 1
    return n * fact(n-1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
print('---------------------------------------------')