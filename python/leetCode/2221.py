# 数组的三角和
class Solution:
    def triangularSum(self, nums):
        while len(nums) > 1:
            tmp = []
            for i in range(len(nums)-1):
                tmp.append((nums[i] + nums[i+1]) % 10)
            nums = tmp

        return nums[0]


