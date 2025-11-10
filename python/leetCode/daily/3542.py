# 将所有元素变为0的最少操作次数
class Solution:
    def minOperations(self, nums):
        s = []
        answer = 0
        for num in nums:
            while s and s[-1] > num:
                s.pop()
            if num == 0:
                continue
            elif not s or s[-1] < num:
                answer += 1
                s.append(num)


        return answer

