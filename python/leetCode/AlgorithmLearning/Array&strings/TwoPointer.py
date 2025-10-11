# 双指针
# 数组拆分Ⅰ
class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans

# 两数之和Ⅱ
class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        left, right = 0, n - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

# 移除元素
class Solution:
    def removeElement(self, nums, val):
        n = len(nums)
        k = 0
        slow = 0
        for fast in range(n):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
                k += 1

        return k

# 最大连续1的个数
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        ans = 0
        count = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                ans = max(ans, count)
                count = 0
        return ans if ans > count else count

# 长度最小的子数组
class Solution:
    def minSubArrayLen(self, target, nums):
        ans = 10 ** 5
        n = len(nums)
        left = 0
        sum_val = 0
        for right in range(n):
            sum_val += nums[right]
            while left <= right and sum_val >= target and (sum_val - nums[left]) >= target:
                left += 1
                ans = min(ans, right - left + 1)
        return 0 if ans == 10 ** 5 else ans
