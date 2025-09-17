# 设计数字容器系统
from collections import defaultdict
import heapq
class NumberContainers:

    def __init__(self):
        self.list = {}
        # 创建值为list的字典，当访问不存在的字典时，自动创建空列表
        # 访问不存在的字典时，自动创建字典
        self.dict = defaultdict(list)

    def change(self, index, number):
        self.list[index] = number
        heapq.heappush(self.dict[number], index)


    def find(self, number):
        if number not in self.dict:
            return -1

        heap = self.dict[number]
        while heap:
            idx = heap[0]
            if self.list.get(idx) == number:
                return idx
            heapq.heappop(heap)

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

def test():
    obj = NumberContainers()
    print(obj.find(10))
    print(obj.change(2, 10))
    print(obj.change(1, 10))
    print(obj.change(3,10))
    print(obj.change(5,10))
    print(obj.find(10))
    print(obj.list)
    obj1 = NumberContainers()
    print(obj1.find(10))
    print(obj1.change(2, 10))
    print(obj1.change(1, 10))
    print(obj1.change(3, 10))
    print(obj1.change(5, 10))
    print(obj1.find(10))
    print(obj1.change(1, 20))
    print(obj1.find(10))
    print(obj1.list)

test()