# 统计公平数对的数目
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums, lower, upper):
        if len(nums) <= 1:
            return 0
        nums.sort()
        answer = 0
        for i in range(len(nums)-1):
            left = bisect_left(nums, lower - nums[i], i+1, len(nums))
            right = bisect_right(nums, upper - nums[i], i+1, len(nums))
            answer += right - left

        return answer

def test():
    s = Solution()
    print(s.countFairPairs([0,1,7,4,4,5], 3, 6))
    print((s.countFairPairs([1, 7, 9, 2, 5], 11, 11)))

test()