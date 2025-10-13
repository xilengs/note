# 最大频率元素计数
class Solution:
    def maxFrequencyElements(self, nums):
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        max = (0, 0)
        for _, value in dict.items():
            if value > max[0]:
                max = (value, 1)
            elif value == max[0]:
                max = (max[0], max[1]+1)

        return max[0] * max[1]

def test():
    s = Solution()
    print(s.maxFrequencyElements([1, 2, 2, 3, 1, 4]))
    print(s.maxFrequencyElements([1, 2, 3, 4, 5]))

test()