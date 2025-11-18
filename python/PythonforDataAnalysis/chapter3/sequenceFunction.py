# enumerate
# 用于追踪当前项的序号
def enumerate_demo():
    some_list = ['foo', 'bar', 'baz']
    mapping = {}
    for i, v in enumerate(some_list):
        mapping[v] = i
    print(f"some_list = {some_list}\nmapping = {mapping}")

# sorted
# 可以从任意序列的元素返回一个新的排好序的列表
def sorted_demo():
    list = [7, 1, 2, 6, 0, 3, 2]
    s = 'horse race'
    print(f"orginal list = {list}\nsorted list = {sorted(list)}")
    print(f"original string = {s}\nsorted string = {sorted(s)}")

# zip
# zip 可以将多个列表、元组或其他序列成对组合成一个元组列表：
def zip_demo():
    seq1 = ['foo', 'bar', 'baz']
    seq2 = ['one', 'two', 'three']
    zipped = zip(seq1, seq2)
    print(f"seq1 = {seq1}\nseq2 = {seq2}\nzipped seq1 and seq2 = {list(zipped)}")
    # zip 可以处理不等长的序列, 元素的个数取决于最短的序列
    seq3 = [False, True]
    zipped2 = zip(seq1, seq2, seq3)
    print(f"seq3 = {seq3}\nzipped seq1, seq2 and seq3 = {list(zipped2)}")
    # 给出一个“被压缩的”序列, zip 可以被用来解压序列
    pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
    first_names, last_names = zip(*pitchers)
    print(f"pitchers = {pitchers}\nfirst_names, last_names = zip(*pitchers)")
    print(f"first_names = {first_names}\nlast_names = {last_names}")
    # zip 可以用来把行序列转换层列序列
    rows = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    columns = list(zip(*rows))
    print(f"rows = {rows}\ncolumns = list(zip(*rows))\ncolumns = {columns}")

def reversed_demo():
    # reversed 可以从后向前迭代一个序列：
    l = [x for x in range(10)]
    rev_l = reversed(l)
    print(f"original list = {l}\nreversed list = {list(rev_l)}")
        

def spilt_line():
    print('-------------------------------------------------------')

if __name__ == '__main__':
    spilt_line()
    enumerate_demo()
    spilt_line()
    sorted_demo()
    spilt_line()
    zip_demo()
    spilt_line()
    reversed_demo()
    spilt_line()