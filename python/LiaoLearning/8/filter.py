# python 内建的filter()函数用于过滤序列
# 和map()类似，filter()也接收一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1,2,4,5,6,9,10,15])))
# 删掉一个序列中的空字符
def not_empty(s):
    # 检查s非空，并去除s首位的空字符
    return s and s.strip()
print(list(filter(not_empty, ['A','', 'B', None, 'C', '  '])))
# filter()函数同样返回的是一个Iterator，也就是一个惰性序列
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list

# 一个从3开始的奇数数列
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n
# 定义一个筛选函数
# 返回lambda函数
def _not_divisible(n):
    return lambda x: x%n > 0
# 生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() #初始化序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
# 输出1-100以内的素数
for n in primes():
    if n < 100:
        print(n)
    else:
        break

# 练习
# 利用filter()筛选出回数
# zip(a, b)会把a[0]和b[0]配成(a[0], b[0]),依次类推
# zip()返回一个迭代器
# zip()会按最短的那个序列长度截断，多余的元素会被丢弃
def is_palindrome(n):
    if n < 10:
        return n
    tmp = n
    l = []
    while tmp != 0:
        l.append(tmp%10)
        tmp = (tmp-tmp%10)/10
    for begin,end in zip(l, reversed(l)):
        if begin != end:
            return False
    return True

def test():
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99,
                                                      101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')

test()