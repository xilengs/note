# 将整数转换为两个无零整数的和
class Solution:
    def getNoZeroIntegers(self, n: int):
        for A in range(1, n):
            B = n - A
            if '0' not in str(A) + str(B):
                return [A, B]
    
def test():
    s = Solution()
    n1 = 2
    n2 = 11
    n3 = 10000
    n4 = 69
    print(s.getNoZeroIntegers(n1))
    print(s.getNoZeroIntegers(n2))
    print(s.getNoZeroIntegers(n3))
    print(s.getNoZeroIntegers(n4))

test()