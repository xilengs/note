# 使数组元素等于零
class Solution:
    def countValidSelections(self, nums):
        answer = 0
        sum_nums = sum(nums)
        left = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                if left == sum_nums / 2:
                    answer += 2
                elif left == (sum_nums - 1) / 2:
                    answer += 1
                elif left == (sum_nums + 1) / 2:
                    answer += 1
            else:
                left += nums[i]


        return answer


def test():
    s = Solution()
    print(s.countValidSelections([16, 13, 10, 0, 0, 0, 10, 6, 7, 8, 7]))

test()
