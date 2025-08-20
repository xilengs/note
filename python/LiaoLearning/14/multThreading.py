# 多线程
# 线程是操作系统直接支持的执行单元
# python的线程是真正的Posix线程，而不是模拟出来的线程
# python的标准库提供了两个模块来处理线程：_thread和threading
# _thread是低级别的线程模块，threading是高级别的线程模块,对_thread进行了封装

# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行

import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t1 = threading.Thread(target=loop, name='LoopThread')
t1.start()
t1.join()  # 等待线程t1结束
print('thread %s ended.' % threading.current_thread().name)

# 由于任何进程默认就会启动一个线程，我们把该线程称为主线程
# 主线程可以启动新的线程，但主线程只能在所有子线程结束后才能结束
# 如果主线程在子线程结束前结束，则子线程会被强制终止

# Lock
# 多线程和多进程的最大区别在于，线程可以共享数据
# 所以任何一个变量都可以被任何一个线程修改
# 假设这是你的银行存款
balance = 0

def change_it(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(10000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('balance = %s' % balance)
# 由于线程是并发执行的，两个线程同时修改balance时可能会出现错误

# 给线程上锁，使用treading.Lock()实现
balance2 = 0
lock = threading.lock()

def run_thread_lock(n):
    for i in range(10000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()