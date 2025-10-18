# 执行操作后不同元素的最大数量
class Solution:
    def maxDistinctElements(self, nums, k):
        nums.sort()
        pre = nums[0] - k
        answer = 1
        for i in range(1, len(nums)):
            tmp = min(max(nums[i]-k, pre+1), nums[i]+k)
            if tmp > pre:
                answer += 1
                pre = tmp
        return answer

def test():
    s = Solution()
    print(s.maxDistinctElements([1,2,2,3,3,4], 2))
    print(s.maxDistinctElements([4,4,4,4], 1))
    print(s.maxDistinctElements([1,1,1,2,2,2,4,4,4,4], 2))

test()


