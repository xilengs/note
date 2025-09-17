# 统计隐藏数组数目
class Solution:
    def numberOfArrays(self, differences, lower, upper):
        num_min, num_max = 0, 0
        num_sum = 0
        for i in differences:
            num_sum += i
            if num_sum < num_min:
                num_min = num_sum
            elif num_sum > num_max:
                num_max = num_sum

        return max(upper-lower-num_max+num_min+1, 0)

def test():
    s = Solution()
    print(s.numberOfArrays([1, -3, 4], 1, 6))
    print(s.numberOfArrays([3, -4, 5, 1, -2], -4, 5))
    print(s.numberOfArrays([4, -7, 2], 3, 6))

test()
