# 设计任务管理器
import heapq
from collections import defaultdict
from heapq import heappush, heappop

from networkx.classes import selfloop_edges


class TaskManager:

    def __init__(self, tasks):
        # 任务字典
        # self.dict = defaultdict(dict)
        # 优先级靠前
        self.prior = defaultdict(list)
        for task in tasks:
            # self.dict[task[0]][task[1]] = task[2]
            # heapq.heappush(self.dict[task[0]], (task[1], task[2]))
            heapq.heappush(self.prior[task[0]], (-task[2], task[1]))
        self.del_task = []
        self.edit_task = {}

    def add(self, userId, taskId, priority):
        # self.dict[userId][taskId] = priority
        # heapq.heappush(self.dict[userId], (taskId, priority))
        heapq.heappush(self.prior[userId], (-priority, taskId))

    def edit(self, taskId, newPriority):
        self.edit_task[taskId] = -newPriority

    def rmv(self, taskId):
        self.del_task.append(taskId)

    def execTop(self):
        best_prior = 1
        best_Id = -1
        best_userId = -1

        for taskId, prior in self.edit_task.items():
            if prior < best_prior or (prior == best_prior and taskId > best_Id):
                if taskId not in self.del_task:
                    best_prior = prior
                    best_Id = taskId

        for Id, prior in self.prior.items():
            while prior and(prior[0][1] in self.del_task or prior[0][1] in self.edit_task):
                top = heapq.heappop(prior)
                if top[1] in self.del_task:
                    if top[1] in self.edit_task:
                        self.edit_task.pop(top[1])
                    self.del_task.remove(top[1])
                elif top[1] in self.edit_task:
                    new_prior = self.edit_task.pop(top[1])
                    heapq.heappush(prior, (new_prior, top[1]))

            if prior:
                top = prior[0]
                if (top[0] < best_prior) or (top[0] == best_prior and top[1] >= best_Id):
                    best_prior = top[0]
                    best_Id = top[1]
                    best_userId = Id


        if best_Id in self.edit_task:
            self.del_task.append(best_Id)
            self.edit_task.pop(best_Id)
            for Id, prior in self.prior.items():
                if any(best_Id == item[1] for item in prior):
                    best_userId = Id

        if best_userId != -1:
            if self.prior[best_userId][0][1] == best_Id:
                heapq.heappop(self.prior[best_userId])
            return best_userId
        else:
            return -1


def test():
    s = TaskManager([[1,101,10], [2, 102, 20], [3, 103, 15]])
    print(s.add(4,104, 5))
    print(s.edit(102, 8))
    print(s.execTop())
    print(s.rmv(101))
    print(s.add(5, 105, 15))
    print(s.execTop())
    s1 = TaskManager([[2, 12, 25], [2, 13, 36], [9, 9, 26]])
    print(s1.execTop())
    s2 = TaskManager([[0,5,27],[3,3,22],[0,6,31],[8,29,18],[5,1,37],[4,2,18],[7,10,39],[1,28,18],[0,20,45],[3,19,15],[9,16,32],[3,24,15],[8,26,43],[0,30,42],[1,8,37],[2,15,47]])
    s2.edit(30, 48)
    s2.rmv(24)
    print(s2.execTop())
    s3 = TaskManager([[7,3,14],[6,1,7],[1,17,19],[4,13,6],[4,26,14],[2,8,43],[7,29,47]])
    print(s3.execTop())
    print(s3.execTop())
    print(s3.execTop())
    s3.edit(13, 45)
    print(s3.execTop())
    print(s3.execTop())
    print("---------------------------------")
    s4 = TaskManager([[8,17,13],[2,20,24],[10,3,12]])
    s4.edit(3, 8)
    s4.add(6, 24, 28)
    s4.rmv(3)
    print(s4.execTop())
    print(s4.execTop())
    s4.edit(17, 1)
    print(s4.execTop())
    s4.add(8, 0, 47)
    s4.rmv(0)
    print(s4.execTop())


test()


def test_task_manager():
    # 初始化任务列表
    tasks = [
        [35, 22, 732], [17, 31, 76], [28, 59, 184], [14, 46, 511],
        [23, 70, 2], [49, 3, 373], [35, 96, 832], [17, 84, 760],
        [34, 65, 591], [5, 99, 198], [50, 55, 948], [26, 25, 692],
        [5, 45, 10], [43, 15, 962], [33, 57, 564], [50, 10, 869],
        [28, 51, 344], [10, 80, 884], [39, 23, 617], [17, 98, 905],
        [48, 7, 660], [46, 78, 156], [15, 63, 766]
    ]

    # 创建 TaskManager 实例
    tm = TaskManager(tasks)

    # 操作序列
    operations = [
        "execTop", "rmv", "rmv", "rmv", "edit", "edit", "rmv", "execTop",
        "execTop", "execTop", "execTop", "execTop", "add", "execTop", "edit",
        "edit", "rmv", "execTop", "rmv", "execTop", "rmv", "execTop", "rmv",
        "rmv", "execTop", "rmv", "rmv", "rmv", "edit", "edit", "add", "edit",
        "edit", "add", "execTop", "execTop", "edit", "add", "add", "rmv",
        "execTop", "add", "edit", "add", "add", "rmv", "rmv", "edit", "rmv",
        "rmv", "execTop", "execTop", "add", "edit", "rmv", "execTop", "add",
        "add", "execTop", "rmv", "add", "execTop", "execTop"
    ]

    # 参数序列
    parameters = [
        [], [31], [23], [70], [25, 300], [25, 171], [45], [], [], [], [], [],
        [41, 83, 655], [], [59, 152], [99, 132], [78], [], [25], [], [59], [],
        [57], [83], [], [99], [51], [3], [46, 922], [46, 374], [22, 51, 802],
        [46, 456], [51, 114], [14, 52, 795], [], [], [51, 1000], [8, 17, 721],
        [18, 34, 77], [17], [], [49, 7, 261], [34, 859], [37, 23, 298],
        [48, 72, 320], [23], [72], [7, 187], [7], [34], [], [], [31, 87, 684],
        [87, 353], [87], [], [39, 29, 704], [34, 98, 766], [], [29],
        [10, 49, 853], [], []
    ]

    # 执行所有操作
    results = []
    for i, op in enumerate(operations):
        params = parameters[i]
        if op == "execTop":
            result = tm.execTop()
            results.append(result)
            print(f"execTop() -> {result}")
        elif op == "add":
            tm.add(params[0], params[1], params[2])
            print(f"add({params[0]}, {params[1]}, {params[2]})")
        elif op == "edit":
            tm.edit(params[0], params[1])
            print(f"edit({params[0]}, {params[1]})")
        elif op == "rmv":
            tm.rmv(params[0])
            print(f"rmv({params[0]})")

    # 返回所有 execTop 的结果
    return results


# 运行测试
if __name__ == "__main__":
    results = test_task_manager()
    print("\n所有 execTop 的结果:")
    for i, result in enumerate(results):
        print(f"execTop {i + 1}: {result}")

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()


class TaskManager:

    def __init__(self, tasks):
        self.taskInfo = {}
        self.heap = []
        for userId, taskId, priority in tasks:
            self.taskInfo[taskId] = [priority, userId]
            heappush(self.heap, [-priority, -taskId])

    def add(self, userId, taskId, priority) -> None:
        self.taskInfo[taskId] = [priority, userId]
        heappush(self.heap, [-priority, -taskId])

    def edit(self, taskId: int, newPriority: int) -> None:
        self.taskInfo[taskId][0] = newPriority
        heappush(self.heap, [-newPriority, -taskId])

    def rmv(self, taskId: int) -> None:
        self.taskInfo.pop(taskId)

    def execTop(self) -> int:
        while self.heap:
            priority, taskId = heappop(self.heap)
            priority, taskId = -priority, -taskId
            if priority == self.taskInfo.get(taskId, [-1, -1])[0]:
                return self.taskInfo.pop(taskId)[1]
        return -1

