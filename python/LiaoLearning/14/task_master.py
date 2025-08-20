import time, random, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

def get_task_queue():
    return task_queue
def get_result_queue():
    return result_queue
# 把两个Queue都注册到网络上，callable参数关联了Queue对象
# Windows下multiprocessing使用spawn启动新进程，spawn会把主进程的函数对象pickle到子进程去，lambda函数是无法被pickle的
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)

# 在windows上，multiprocessing默认使用spawn方式启动新进程，子进程会重新导入主模块
# 如果没有if __name__ == '__main__':，子进程会重新执行主模块的代码，导致死循环
# 因此，必须把主模块的代码放在if __name__ == '__main__':下
if __name__ == '__main__':
    QueueManager.register('get_task_queue', callable=get_task_queue)
    QueueManager.register('get_result_queue', callable=get_result_queue)    

    # 绑定端口5000，设置验证码'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()
    # 通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=100)
        print('Result: %s' % r)
    # 关闭
    manager.shutdown()
    print('master exit.')
# 运行这个脚本时，确保先启动worker进程