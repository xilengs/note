# python内置的sorted()函数可以对list进行排序
def mysorted():
    l = [36, 5, -12, 9, -21]
    print(sorted(l))
    # sorted()函数也是一个高阶函数，可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
    print(sorted(l, key=abs))
    # key指定函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。

    # 字符串排序
    ls = ['bob', 'about', 'Zoo', 'Credit']
    print(sorted(ls))
    # 因为'Z' < 'a'，所以大写字母Z会排在小写字母'a'的前面
    # 忽略大小写进行排列
    print(sorted(ls, key=str.lower))
    # 反向排序
    print(sorted(ls, key=str.lower, reverse=True))

mysorted()

# 练习
# 用一组tuple表示学生名字和成绩，用sorted()函数对列表进行名字排名
# 再按成绩从高到低排序
def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

def test():
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2 = sorted(L, key=by_name)
    print(L2)
    L2 = sorted(L, key=by_score)
    print(L2)

test()
