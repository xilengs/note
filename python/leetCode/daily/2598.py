# 执行操作后的最大MEX
class Solution:
    def findSmallestInteger(self, nums, value):
        n = len(nums)
        list1 = [0] * value
        for i in range(n):
           list1[nums[i] % value] += 1
        least = (0, 10 ** 9 + 1)
        for i in range(len(list1)):
            if list1[i] < least[1]:
                least = (i, list1[i])
        return least[1] * value + least[0]

def test():
    s = Solution()
    print(s.findSmallestInteger([1, -10, 7, 13, 6, 8], 5))
    print(s.findSmallestInteger([1, -10, 7, 13, 6, 8], 7))
    print(s.findSmallestInteger([-5, -3, 0, 0, 1, 2, 3, 4], 2))
    print(s.findSmallestInteger([-2], 5))

test()