# StringIO and BytesIO
# StringIO 在内存中读写数据
from io import StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('world!')
# getvalue()方法用于获得写入后的str
print(f.getvalue())

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
# strip()默认去掉字符串首尾的空白字符
# 也可以传入字符串参数，告诉strip()去掉那些字符
s = '----Hello,world!----'
print(s.strip("-"))
s1 = 'xyxhelloxy'
# 去掉首位的x和y，直到遇到不是这两个字符
print(s1.strip('xy'))
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO
# StringIO只能操作str,如果要操作二进制数据，就要使用BytesIO
# BytesIO实现在内存中读写Bytes
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())