# 计算子数组的 x-sum Ⅰ
from collections import Counter
class Solution:
    def findXSum(self, nums, k, x):
        answer = []
        for i in range(len(nums) - k + 1):
            items = Counter(nums[i:i+k]).items()
            items = sorted(items, key=lambda item:(item[1], item[0]), reverse=True)
            answer.append(sum([item[0] * item[1] for item in items[:x]]))
        return answer


def test():
    s = Solution()
    print(s.findXSum([1,1,2,2,3,4,2,3], 6, 2))

test()



