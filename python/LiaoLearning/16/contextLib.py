# contextlib
# 读写文件需要注意每次读写完成后关闭文件，可以通过try...finally来正确关闭，防止忘记写close()函数
# 用with语句可以简化代码
# 任何对象只要正确实现上下文管理，都可以使用with语句
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的
class Query(object):
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print('Begin')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('error')
        else:
            print('End')
    
    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()

# @contextmanager
# 编写__enter__和__exit__仍然很繁琐，下面是更简单的写法
from contextlib import contextmanager

class QueryA(object):
    def __init__(self, name):
        self.name = name
    
    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_queryA(name):
    print('Begin')
    q = QueryA(name)
    yield q 
    print('End')

with create_queryA('Bob') as q:
    q.query()

# 如果一个对象没有实现上下文，我们就不能把它用于with语句。
# 可以用closing()来把该对象变为上下文对象。例如，with语句使用urlopen()
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

# closing也是一个经过@contextmanager装饰的generator
# 把任意对象变成上下文对象
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()