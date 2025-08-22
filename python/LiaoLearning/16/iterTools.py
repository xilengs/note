# itertools
import itertools
# itertools.count(start=0, step=1),无限的迭代器，生成等差数列
natuals = itertools.count(1)
# cycle()会把传入的一个序列无限重复下去,每次输出序列中一个字符
cs = itertools.cycle('ABC')
# repeat()负责把一个元素无限重复下去，提供第二个参数可以限定重复次数
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

# 通过takewhile()等函数根据条件判断来截取出一个有限序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
# 只迭代一次
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby()
# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

# 练习
# 计算圆周率可以根据公式：
# Π / 4 = 1 - 1/3 + 1/5 - 1/7...
def pi(N):
    l = [x for x in range(2*N+1) if x % 2 == 1]
    l = [4/x if x % 4 == 1 else -4/x for x in l]
    sum = 0
    for x in l:
        sum += x
    return sum
    
def test():
    # 测试:
    print(pi(10))
    print(pi(100))
    print(pi(1000))
    print(pi(10000))
    assert 3.04 < pi(10) < 3.05
    assert 3.13 < pi(100) < 3.14
    assert 3.140 < pi(1000) < 3.141
    assert 3.1414 < pi(10000) < 3.1415
    print('ok')

test()