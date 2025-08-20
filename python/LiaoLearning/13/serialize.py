# 序列化
# 在程序运行过程中，所有变量都存储在内存中，可以修改变量。
# 程序结束后，变量所占用的内存就被操作系统全部回收
# 把变量从内存中变成可存储或传输的过程称之为序列化，在python中叫picking
# 序列化之后，就可以把序列化后的内容写入到磁盘，或者通过网络传输到别的机器上
# 反过来，把变量内容从序列化的对象重新读取到内存里称之为反序列化，即unpicking
# python提供了pickle模块来实现序列化
import pickle

d = dict(name='Bob', age=20, score=88)
# pickle.dumps()把任意对象序列化成一个bytes
pickle.dumps(d)
# pickle.dump()直接把对象序列化后写入一个file-like Object
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 反序列化
f = open('dump.txt', 'rb')
da = pickle.load(f)
f.close()
print(da)

# JSON
# 在不同的编码语言之间传递对象，就必须把对象序列化为标准格式
# 比如XML，但更好的方法是序列化为JSON
# 因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
# JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，十分方便
# JSON表示的对象就是标准的JavaScript语言的对象，JSON和python内置的数据类型对应如下
"""
JSON        |       python类型
{}          |       dict
[]          |       list
"string"    |       str
1234.56     |       int/float
true/false  |       True/False
null        |       None
"""
# python内置的json模块提供了非常完善的python对象到JSON格式的转换
import json
# dumps()返回一个str,内容就是标准JSON
# 类似的，dump()方法可以直接把JSON写入一个file-like Object中读取字符串并反序列化
print(json.dumps(d))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
# JSON标准规定JSON编码是UTF-8

# JSON进阶
# python的dict对象可以直接序列化为JSON的{}，不过很多时候更需要序列化class
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
# 直接序列化，json不知道如何把class转换为json,需要写一个转化函数
# (json.dumps(s))
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))

# 中文序列化
# ensure_ascii默认为True,把中文字符转换为ascii形式再存储
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
a = json.dumps(obj, ensure_ascii=False)
print(a)