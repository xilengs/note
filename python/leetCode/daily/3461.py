# 判断操作后字符串中的数字是否相等Ⅰ
class Solution:
    def hasSameDigits(self, s):
        nums = list(map(int, s))
        n = len(nums)
        while n > 2:
            for i in range(n-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            n -= 1
        return False if nums[0] != nums[1] else True