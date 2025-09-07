from math import floor

class Solution:
    def get(self, num: int) -> int:
        i = 1
        base = 1
        cnt = 0
        while base <= num:
            cnt += ((i + 1) // 2) * (min(base * 2 - 1, num) - base + 1)
            i += 1
            base *= 2
        return cnt

    def minOperations(self, queries) -> int:
        res = 0
        for q in queries:
            res += (self.get(q[1]) - self.get(q[0] - 1) + 1) // 2
        return res
        

def test():
    q1 = [[1,2], [2,4]]
    q2 = [[2,6]]
    s = Solution()
    print(s.minOperations(q1))
    print(s.minOperations(q2))

test()