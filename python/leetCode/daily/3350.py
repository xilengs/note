# 检测相邻递增子数组Ⅱ
class Solution:
    def maxIncreasingSubarrays(self, nums) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
        
        max_k = 0
        last_end = dp[0]
        for i in range(1, n):
            if dp[i] == 1:
                    max_k = max(max_k, min(dp[i-1], last_end), last_end // 2)
                    last_end = dp[i-1]
        max_k = max(max_k, min(dp[n-1], last_end), last_end // 2, dp[n-1] // 2)
        
        return max_k

def test():
    s = Solution()
    print(s.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]))
    print(s.maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7]))
    print(s.maxIncreasingSubarrays([-16, -4, 14, -9, 13]))

test()

        