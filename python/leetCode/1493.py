# 给你一个二进制数组nums，你需要从中删掉一个元素。
# 请你在删掉元素的结果数组中，返回最长的且只包含1的非空子数组的长度。
# 如果不存在这样的子数组，请返回0

# 无敌复杂版本，先维护一个数组，找到每个元素前面有多少个连续的1，并记录下最长的1子段长度
# 然后遍历数组，在找到0时，看看左右两边是不是1，如果是，就进行拼接，并与现有的最长字段进行比较，如果更长，则修改
class Solution1:
    def longestSubarray(self, nums) -> int:
        if not 0 in nums:
            return len(nums) - 1
        if not 1 in nums:
            return 0
        l = len(nums)
        num = [0] * l
        num[0] = nums[0]
        bigest = num[0]
        for i in range(1, l):
            if nums[i] == 1:
                num[i] = num[i-1] + 1
                bigest = max(bigest, num[i])
            else:
                num[i] = 0

        length = 0
        for i in range(1, l-1):
            if num[i] == 0:
                if i-1 >=0 and num[i-1] and num[i+1]:
                    for j in range(i+1, l):
                        if not num[j]:
                            length = max(length, num[i-1]+num[j-1])
                            break
                    else:
                        length = max(length, num[i-1]+(l-i-1))
        
        return max(length,bigest) if length else bigest


# 滑动窗口法，只允许窗口里最多有一个0
class Solution:
    def longestSubarray(self, nums) -> int:
        left = 0
        zeros = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            # 窗口里最多允许一个 0
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # 删除一个 0 后的最大长度
            res = max(res, right - left)

        return res


def test():
    nums = [1,1,0,1]
    s= Solution()
    print(s.longestSubarray(nums))

test()