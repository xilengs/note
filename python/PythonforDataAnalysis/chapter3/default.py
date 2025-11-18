from collections import defaultdict

def dict_usage():
    spilt_line()
    # 下面的逻辑很常见
    """
    if key in some dict:
        value = some_dict[key]
    else:
        value = default_value
    """
    # dict 的 get 和 pop 函数可以取默认值返回, 上面的if-else语句可以简写成下面:
    """
    value = some_dict.get(key, default_value)
    """

    words = ['apple', 'bat', 'bar', 'atom', 'book']
    by_letter = {}
    for word in words:
        letter = word[0]
        if letter not in by_letter:
            by_letter[letter] = [word]
        else:
            by_letter[letter].append(word)
    print(f"by_letter: {by_letter}")

    # setdefault
    # 获取一个键的值, 如果这个键不存在, 他会设置一个默认值, 然后返回这个默认值
    # 简化上面的代码
    by_letters = {}
    for word in words:
        by_letters.setdefault(word[0], []).append(word)
    print(f"by_letters: {by_letters}")

    # defaultdict
    # 传递类型或者函数以生成每个位置的默认值
    # defaultdict 可以进一步简化上述代码
    by_letters_defaultdict = defaultdict(list)
    for word in words:
        by_letters_defaultdict[word[0]].append(word)
    print(f"by_letters_defaultdict: {by_letters_defaultdict}")

    # 字典的值可以是任意 Python 对象, 但键通常是不可变的标量类型(整数、浮点数、字符串)或元组
    # 这通常被称为"可哈希性", 可以用 hash 函数检测一个对象是否是可哈希的

def set_usage():
    spilt_line()
    # 无序的不可重复的元素的集合
    # 集合支持合并、交集、差分和对称差等数学集合运算
    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7, 8}
    print(f"a = {a}\n b = {b}")
    print(f"合并：\na.union(b) = {a.union(b)}\na | b = {a | b}")
    print(f"交集：\na.intersection(b) = {a.intersection(b)}\na & b = {a & b}")

def list_comprehension():
    spilt_line()
    # 列表推导式的for部分是根据嵌套的顺序, 过滤条件放在最后
    some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    flattened = [x for tup in some_tuples for x in tup]
    print(f"some_tuples = {some_tuples}")
    print(f"flattened some_tuples = {flattened}")
    # 等同于嵌套 for 循环
    """
    for tup in some_tuples: 
        for x in tup:
            pass
    """


def spilt_line():
    print('-------------------------------------------------------')

if __name__ == "__main__":
    dict_usage()
    set_usage()
    list_comprehension()