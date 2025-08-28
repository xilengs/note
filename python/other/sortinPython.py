# python中对列表进行排序的五种方法
# sort(),就地排序，可以直接对列表进行排序，不需要创建新的列表
# sort()有两个可选参数reverse和key
# reverse参数是一个布尔值，用于指定排序顺序是升序还是降序,默认为False(升序)
# key参数是一个函数，用于指定排序的关键字，默认为None，表示按照元素的大小排序
print('sort()')
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True) # 降序排列
print(lst)

lst = ['apple', 'banana', 'orange', 'pear']
print(lst)
lst.sort(key=len)
print(lst)

# sorted()函数返回一个新的已排序列表，不影响原列表
# sorted()有三个参数， reverse、key和cmp
# reverse和key同上
# cmp参数是一个函数，用于指定两个元素比较的规则，默认为None
print('------------------------------------------')
print('sorted()')
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
new_lst = sorted(lst)
print(lst, "-------", new_lst)
new_lst = sorted(lst, reverse=True)
print(new_lst)

lst = ['apple', 'banana', 'orange', 'pear']
new_lst = sorted(lst, key=len)
print(new_lst)

# lambda表达式作为key参数进行排序
print('----------------------------------------')
print('用lambda表达式作为key参数进行排序')
lst = ['apple', 'banana', 'orange', 'pear']
lst.sort(key=lambda x: x[1])
print(lst)

# 使用operator模块进行排序
# 使用operator模块中的函数作为key参数，指定排序的关键字
print('--------------------------------------')
import operator

lst = [('apple', 3), ('banana', 2), ('orange', 4), ('pear', 1)]
lst.sort(key=operator.itemgetter(1))
print(lst)

# 使用numpy模块进行排序
print('-----------------------------------------')
import numpy as np

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
new_lst = np.sort(lst)
print(new_lst)

new_lst = np.sort(lst)[::-1]
print(new_lst)