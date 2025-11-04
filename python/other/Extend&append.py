# extend  和 append 都是像末尾加元素
# 不同的是 extend 会把 item 作为一个可迭代对象，迭代的将item中的元素加入末尾
# append 则是将 item 作为一个整体加入末尾
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"list1: {list1}\nlist2: {list2}")
list1.extend([4,5])
list2.append([4,5])
print(f"list1: {list1}\nlist2: {list2}")
list1.extend('abc')
list2.append('abc')
print(f"list1: {list1}\nlist2: {list2}")
