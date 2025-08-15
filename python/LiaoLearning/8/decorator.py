import functools
import time
# 函数有一个__name__属性，可以拿到函数的名字：
# 在代码运行期间动态增加功能的方式，称之为“装饰器”(Decorator)
# 本质上，decorator就是一个返回函数的高阶函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 把decorator置于函数的定义处：
# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)
@log
def now():
    print('2025.8.14')

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def log_on(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# now_on = log_on('execute')(now)
@log_on('execute')
def now_on():
    print('2025-8-14')

# 一个完整的decorator写法：
# @functools.wraps()把原始函数名字复制到wrapper()中
def log_full(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log_full
def now_full():
    print('2025-8-14')

# 或者针对带参数的decorator：
def log_full_args(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log_full_args('today function:')
def now_full_args():
    print('2025-8-14')

def decorator():
    f = now
    f()
    print(now.__name__)
    print(f.__name__)
    now_on()
    print(now_on.__name__)
    now_full()
    now_full_args()

decorator()

# 练习
# 设计一个decorator,可作用于任何函数上，并打印该函数的执行时间
print('-----------------------------------------------')
def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.perf_counter()
        result = func(*args, **kw)
        end = time.perf_counter()
        print('%s() 运行时间: %s' % (func.__name__, end - start))
        return result
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

def log_new(text=None):
    def decorator(func, out=None):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if out:
                print(out)
            print('now function: %s' % func.__name__)
            return func(*args, **kw)
        return wrapper

    if callable(text):
        return decorator(text)
    elif isinstance(text,str):
        out = '输入的是字符串：' + text
    elif isinstance(text, (int,float)):
        out = '输入的是数值: %s' % text
    return lambda func: decorator(func, out)

@log_new('Oi')
def now_new_str():
    print('2025-8-14')

@log_new(14.3)
def now_new_number():
    print('2025-8-14')

@log_new
def now_new_none():
    print('2025-8-14')


def test():
    f = fast(11, 22)
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')
    m = now_new_str
    n = now_new_number
    l = now_new_none
    m()
    n()
    l()


test()
print('-----------------------------------------------')