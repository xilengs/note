# 有效三角形的个数
class Solution:
    def triangleNumber(self, nums):
        n = len(nums)
        if n < 3:
            return 0
        answer = 0
        nums.sort()
        for i in range(n-2):
            for j in range(i+1, n-1):
                left, right, k = j + 1, n - 1, j
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                answer += k - j

        return answer

def test():
    s = Solution()
    print(s.triangleNumber([2, 2, 3, 4]))
    print(s.triangleNumber([4, 2, 3, 4]))

test()