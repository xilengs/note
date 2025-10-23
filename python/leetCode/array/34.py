# 在排序数组中查找元素的第一个和最后一个位置
class Solution:
    def searchRange(self, nums, target):
        n = len(nums)
        left, right = 0, n-1
        start, end = 0, 0
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif target == nums[mid]:
                start, end = mid, mid
                for i in range(mid, -1, -1):
                    if nums[i] == target:
                        start = i
                    else:
                        break
                for i in range(mid, n):
                    if nums[i] == target:
                        end = i
                    else:
                        break
                return [start, end]
        return [-1, -1]


                
        