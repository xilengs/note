from functools import reduce

# map()接收两个参数，一个函数，一个式Iterable
# map()将传入的参数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f(x):
    return x*x
# map()传入的第一个参数是f，即函数对象本身
# 由于r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来返回一个list
L = [x for x in range(1,10)]
print(L)
r = map(f,L)
print(list(r))
# map()把运算规则抽象了，因此，可以计算任意复杂函数
print(list(map(str, L)))

# reduce()把一个函数作用在一个序列[x1,x2,...xk]上，这个函数必须接收两个参数(这个函数指的是传入的reduce的函数)
# reduce()把结果继续和序列的下一个元素做累计计算：
# reduce(f, [x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
def add(x,y):
    return x+y
print(reduce(add,[1,3,5,7,9]))
# 把序列[1,3,5,7,9]变成13579
def fn(x,y):
    return x*10 + y

print(reduce(fn,[1,3,5,7,9]))

# 把str转换成int的函数
def char2num(s):
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    return digits[s]

print(reduce(fn, map(char2num, '13579')))

# 练习
# 使用map() 把用户输入的不规范的英文名字变成首字母大写，其他小写的规范名字
# map()在传入list时，把list里的参数一个一个传入
def normalize(l1):
    return l1[0].upper()+l1[1:].lower()

def test1():
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)

# 编写一个函数可以接受一个list并利用reduce()求积
def sumNumber(x,y):
    return x*y

def prod(L):
    return reduce(sumNumber,L)

def test2():
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')

# 利用map()和reduce()编写一个函数，把内容为浮点数的字符串转换为浮点数
# 通过split()函数将s直接分割为整数部分和小数部分
def str2float(s):
    if '.' in s:
        integer_part, decimal_part = s.split('.')
    else:
        integer_part, decimal_part = s, ''
    int_num = reduce(fn,map(char2num, integer_part))
    if decimal_part:
        dec_num = reduce(fn, map(char2num, decimal_part))
        dec_num = dec_num / (10 ** len(decimal_part))
    else:
        dec_num = 0
    return int_num + dec_num

def test3():
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')

test1()
test2()
test3()