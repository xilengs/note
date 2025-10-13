# 三角形的最大周长
class Solution:
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] < nums[j] + nums[k]:
                        return nums[i] + nums[j] + nums[k]
                    else:
                        break
        else:
            return 0

def test():
    s = Solution()
    print(s.largestPerimeter([2, 1, 2]))

test()
