# 仅含置位位的最小整数
class Solution:
    def smallestNumber(self, n) :
        i = 0
        while True:
            if 2 ** i - 1 >= n:
                return 2 ** i - 1
            i += 1
