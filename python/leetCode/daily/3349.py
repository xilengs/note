# 检测相邻递增子数组Ⅰ
class Solution:
    def hasIncreasingSubarrays(self, nums, k):
        n = len(nums)
        if n < 2 * k:
            return False
        for i in range(n - 2 * k + 1):
            increasing = True
            for j in range(i, i + k - 1):
                if nums[j] >= nums[j + 1]:
                    increasing = False
                    break
            if not increasing:
                continue
            increasing = True
            for j in range(i + k, i + 2 * k - 1):
                if nums[j] >= nums[j + 1]:
                    increasing = False
                    break
            if increasing:
                return True
        return False


def test():
    s = Solution()
    print(s.hasIncreasingSubarrays([2, 5, 7, 8, 9, 2,3,4,3,1], 3))
    print(s.hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7],5))

test()