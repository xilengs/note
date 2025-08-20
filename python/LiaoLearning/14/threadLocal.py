# 局部变量只有线程自己能看见，不会影响其他线程，但在函数调用时传递起来很麻烦
# 全局变量会被所有线程共享，全局变量修改必须加锁
"""
def process_student(name):
    std = Student(name)
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)
"""
# 用一个全局变量dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象
"""
global_dict = {}

def std_thread(name):
    std = Student(name)
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()

def do_task_1():
    std = global_dict[threading.current_thread()]
    ...

def do_task_2():
    std = global_dict[threading.current_thread()]
    ...
"""
# 更简单的方法，使用ThreadLocal,不用查dict，ThreadLocal内部会处理好
import threading

# 创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()