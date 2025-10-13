# 四数之和
class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        if n < 4:
            return []
        
        nums.sort()
        res = []

        tmp1 = nums[n-1] + nums[n-2] + nums[n-3]
        tmp2 = nums[n-1] + nums[n-2]
        for i in range(n-3):
            if nums[i] + nums[i+1] +nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + tmp1 < target:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n-2):
                tmp3 = nums[i] + nums[j]
                if tmp3 + nums[j+1] + nums[j+2] > target:
                    break
                if tmp3 + tmp2 < target:
                    continue
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

        return res