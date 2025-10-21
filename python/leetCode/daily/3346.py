# 执行操作后元素的最高频率Ⅰ
class Solution:
    def maxFrequency(self, nums, k, numOperations):
        nums.sort()
        ans = 0
        num_count = {}
        last_num_index = 0
        for i in range(len(nums)):
            if nums[i] != nums[last_num_index]:
                num_count[nums[last_num_index]] = i - last_num_index
                ans = max(ans, i - last_num_index)
                last_num_index = i

        num_count[nums[last_num_index]] = len(nums) - last_num_index
        ans = max(ans, len(nums) - last_num_index)

        for i in range(nums[0], nums[-1] + 1):
            l = bisect.bisect_left(nums, i - k)
            r = bisect.bisect_right(nums, i + k) - 1
            if i in num_count:
                temp_ans = min(r - l + 1, num_count[i] + numOperations)
            else:
                temp_ans = min(r - l + 1, numOperations)
            ans = max(ans, temp_ans)

        return ans


def test():
    s = Solution()
    print(s.maxFrequency([1,4,5], 1, 2))
    print(s.maxFrequency([5,11,20,20], 5, 1))
    print(s.maxFrequency([1, 90], 76, 1))

test()

