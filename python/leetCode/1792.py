from heapq import heapify
from heapq import heapreplace

class Entry:
    __slots__ = 'p', 't'

    def __init__(self, p, t):
        self.p = p
        self.t = t

    # 自定义小于运算符
    # 在使用堆，python通过__lt__()比较两个元素的大小
    def __lt__(self, b:'Entry')->bool:
        return (self.t - self.p) * b.t*(b.t+1) > (b.t-b.p)*self.t*(self.t+1)
    

class Solution:
    def maxAverageRatio(self, classes, extraStudents) -> float:
        h = [Entry(*c) for c in classes]
        heapify(h)
        for _ in range(extraStudents):
            heapreplace(h, Entry(h[0].p+1, h[0].t+1))
        return sum(e.p / e.t for e in h) / len(h)