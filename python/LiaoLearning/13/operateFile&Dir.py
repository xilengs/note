import os
print(os.name)
# uname()在windows上不提供
# print(os.uname())

# 环境变量
print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')
print(os.environ.get('PATH'))

#操作文件和目录
# 查看当前目录的绝对路径：
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录
os.mkdir('C:/D/code/note/python/LiaoLearning/12/testdir')
# 删除目录
os.rmdir('C:/D/code/note/python/LiaoLearning/12/testdir')
# 把两个路径合并
r = os.path.join('C:/D/code/note/python/LiaoLearning', '12/myfile.txt')
# 拆分路径,后一部分总是最后级别的目录或文件名
r1, r2 = os.path.split('C:/D/code/note/python/LiaoLearning/12/myfile.txt')
print(r, r1, r2)
# os.path.splitext()可以直接得到文件扩展名
expand = os.path.splitext(r)
print(expand)
# 对文件重命名
# os.rename('test.txt', 'test.py')
# 删掉文件
# os.remove('test.py')
# 列出当前目录下所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出所有.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.md'])

# 练习
# 1.利用os模块编写一个能实现dir -l输出的程序
# dir_l.py
# 2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印处相对路径
# findStr.py