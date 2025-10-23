# 字符串转换整数
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31
class Solution:
    def myAtoi(self, s):
        num = 0
        s = s.strip()
        if not s:
            return 0
        symbol = 1
        index = 0
        if s[0] == '-':
            symbol = -1
            index += 1
        elif s[0] == '+':
            index += 1

        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            if symbol == 1 and (num > (INT_MAX - digit) // 10):
                return INT_MAX
            if symbol == -1 and (num > (-INT_MIN - digit) // 10):
                return INT_MIN
        
            num = num * 10 + digit
            index += 1
        
        return num * symbol

def test():
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi(" -042"))
    print(s.myAtoi("1337c0d3"))
    print(s.myAtoi("-91283472332"))

test()
