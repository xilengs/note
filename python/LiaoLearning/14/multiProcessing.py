# 多进程
# python的os模块封装了常见的系统调用，其中就包括fork，可以在python程序中轻松创建子进程
import os
from turtledemo.penrose import start

print('Process (%s) start...' % os.getpid())
# 但是windows平台不支持fork()调用
"""
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just create a child process (%s).' % (os.getpid(), pid))
"""

# multiprocessing
# 跨平台版本的多进程模块
from multiprocessing import Process

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    # 等待子进程结束后再继续往下运行
    p.join()
    print('Child process end.')

# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    # 获取当前时间戳
    start = time.time()
    # random.random() 返回一个[0.0, 1.0)区间的浮点随机值
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # 维护一个进程池
    # Pool.map(func, iterable)
    # 类似于map(),把可迭代对象里的元素分配给进程池处理，会等待所有任务完成后返回结果
    # Pool.apply(func, args)
    # 提交一个任务，阻塞执行，直到完成才返回结果
    #Pool.apply_async(func, args)
    # 提交一个任务，异步执行，返回一个AsyncResult对象，可以同.get()拿结果
    # Pool.close()+Pool.join()
    # close():关闭进程池,不能再提交新任务
    # join():等待进程池里的任务执行完毕
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done')
    p.close()
    p.join()
    print('All subprocesses done.')

# 子进程
# subprocess 模块可以非常方便地启动一个子进程，然后控制其输入和输出
# subProcessing.py