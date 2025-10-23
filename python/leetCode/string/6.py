# z 字形变换
class Solution:
    def convert(self, s, numRows):
        if len(s) == 1 or numRows == 1:
            return s
        
        lists = [[] for _ in range(numRows)]
        n = numRows - 1
        row = 0
        # 0 向下， 1向上
        dir = 0
        for i in range(len(s)):
            lists[row].append(s[i])
            if row == 0:
                dir = 0
            elif row == n:
                dir = 1
            if dir:
                row -= 1
            else:
                row += 1

        answer = ''
        for list in lists:
            answer += ''.join(list)
        return answer



def test():
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))

test()
        