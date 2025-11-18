# 是否所有1都至少相隔k个元素
class Solution:
    def kLengthApart(self, nums, k: int):
        last = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if last != -1 and (i - last) < k + 1:
                    return False
                last = i
        return True


def test():
    nums = [1,0,0,0,1,0,0,1]
    s = Solution()
    print(s.kLengthApart(nums, 2))

test()