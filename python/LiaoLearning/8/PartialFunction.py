import functools
# int()函数可以把字符串转换成整数，当仅传入字符串时，int()函数默认按十进制转换

def int2(x, base=2):
    return int(x,base)

def partial():
    print(int('12345'))
    # int()还提供额外的base参数，默认值为10，如果传入base参数，就可以做N进制的转换：
    print(int('12345', base=8))
    # 假设要转换大量二进制字符串，可以定义一个函数
    print(int2('1000000'))
    print(int2('1010101'))

partial()
# functools.partial就是帮助我们创建一个偏函数，不需要我们自己定义int2()

int2_partial = functools.partial(int, base=2)
print(int2_partial('1000000'))
print(int2_partial('1010101'))

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这三个参数
# 当传入：
max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，即
max2(5,6,7)
# 相当于max(10,5,6,7)