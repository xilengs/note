# 找到数组的中间位置
class Solution:
    def findMiddleIndex(self, nums):
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            if left * 2 == total - nums[i]:
                return i
            left += nums[i]
        return -1

def test():
    s = Solution()
    print(s.findMiddleIndex([1, 7, 3, 6, 5, 6]))
    print(s.findMiddleIndex([1, 2, 3]))
    print(s.findMiddleIndex([2, 1, -1]))
    print(s.findMiddleIndex([3,-4,1,-4]))

test()

# 合并区间
class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals)
        ans = []
        ans.append(intervals[0])
        for i in range(1, len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1] = [ans[-1][0], max(ans[-1][1], intervals[i][1])]
            else:
                ans.append(intervals[i])
        return ans
            


