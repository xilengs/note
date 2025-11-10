# 总结
# 反转字符串张的单词Ⅲ
class Solution:
    def reverseWords(self, s):
        words = s.split(" ")
        words = [word[::-1] for word in words]
        ans = " ".join(words)
        return ans

# 寻找旋转排序数组中的最小值
class Solution:
    def findMin(self, nums):
        n = len(nums)
        left, right = 0, n - 1
        if nums[right] < nums[right-1]:
            return nums[right]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]

# 删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        slow = 0
        for fast in range(1, n):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

# 移动零
class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        slow = 0
        k = 0
        for fast in range(n):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            else:
                k += 1
        for i in range(k):
            nums[slow + i] = 0