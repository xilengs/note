# 文件读写
# 读写文件就是请求操作系统打开一个文件对象（通常为文件描述符），然后通过操作系统提供的接口从这个文件对象中读取数据，或者写入数据到这个文件对象

# 读文件
# 以读文件模式打开一个文件对象
f = open('myfile.txt', 'r')
# print(f.read())
for x in f:
    print(x)
# 如果文件不存在，open()函数会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：
"""
>>> f = open('/Users/michael/notfound.txt', 'r')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
FileNotFoundError: [Error 2] No such file or directory: '/Users/michael/notfound.txt')
"""
# 关闭文件
f.close()
# 由于文件读写时都有可能产生IOError,一旦出错，后面的f.close()就不会调用了
# 为了确保文件可以正常关闭，可以使用try...finally来实现
try:
    f = open('myfile.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 这么写太繁琐了，引入with语句自动调用close()方法
with open('myfile.txt', 'r') as f:
    print(f.read())

# read()会一次性读取文件的全部内容，容易爆内存。
# 可以反复调用read(size)方法，每次最后读取size个字节的内容
# 调用readline()可以每次读取一行内容
# 调用readlines()一次读取所有内容并按行返回list
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉

# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在python中统称file-like Object
# 处了file外，还可以是内存的字节流，网络流，自定义流等等
# file-like Object不要求从特定类继承，只要写个read()方法就行
# stringIO就是在内存中创建的file-like Object,常用作临时缓冲

# 二进制文件
# 读取二进制文件
f = open('/User/michael/test.jpg', 'rb')
f.read()

# 读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
# 例如读取GBK编码的文件
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
f.read()
# 遇到编码不规范的文件，可能会遇到UnicodeDecodeError,因为在文本文件中可能夹杂了一些非法编码的字符
# 使用open()函数中的error参数处理
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', error='ignore')


# 写文件
f = open('myfile.txt', 'w')
f.write('Hello, world!')
f.close()
# 当我们写入数据时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入
# 只有调用close()函数操作系统才保证把没有写入的数据全部写入磁盘
with open('myfile.txt', 'w') as f:
    f.write('Hello, world!')
# 要写入特定编码的文本文件，给open()函数传入encoding参数
# 以'w'模式写入文件，会直接覆盖已存在文件
# 用'a'以追加模式写入