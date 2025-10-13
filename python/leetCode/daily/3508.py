# 设计路由器
from collections import deque
from bisect import bisect_left, bisect_right
class Router:

    def __init__(self, memoryLimit):
        self.queue = deque(maxlen=memoryLimit)
        self.sorted_list = []

    def addPacket(self, source, destination, timestamp):
        if (timestamp, source, destination) in self.sorted_list:
            return False
        self.queue.append([source, destination, timestamp])
        self.sorted_list.append((timestamp, source, destination))
        return True

    def forwardPacket(self):
        if len(self.queue) == 0:
            return []
        self.sorted_list = self.sorted_list[1:]
        return self.queue.popleft()

    def getCount(self, destination, startTime, endTime):
        left = bisect_left(self.sorted_list[0], startTime)
        right = bisect_right(self.sorted_list[0], endTime)
        answer = 0
        for index in range(left, right):
            if self.sorted_list[index][2] == destination:
                answer += 1
        return answer

def test():
    r = Router(3)
    print(r.addPacket(1, 4, 90))
    print(r.addPacket(2, 5, 90))
    print(r.addPacket(1, 4, 90))
    print(r.addPacket(3, 5, 95))
    print(r.addPacket(4, 5, 105))
    print(r.forwardPacket())
    print(r.addPacket(5, 2, 110))
    print(r.getCount(5, 100, 110))

test()
# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
