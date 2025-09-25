# 正则表达式
class Solution:
    def isMatch(self, s, p):
        l1, l2 = len(s), len(p)
        if not l1 or not l2:
            return False
        dp = [[False] * l1 for _ in range(l2)]
        if s[0] == p[0] or p[0] == '.' or (p[1] == '*'):
            dp[0][0] = True
        else:
            return False
        print(dp)
        for i in range(1,l2):
            for j in range(1, l1):
                if s[j] == p[i] and dp[i-1][j-1]:
                    dp[i][j] = True
                elif p[i] == '.' and dp[i-1][j-1]:
                    dp[i][j] = True
                elif p[i] == '*' and (p[i-1] == s[j] or p[i-1] == '.') and dp[i-1][j-1]:
                    dp[i][j] = True
                elif p[i-1] == '*' and (i >=3 or dp[i-3][j-1]) and p[i] == s[j]:
                    dp[i][j] = True

        return dp[l2-1][l1-1]

def test():
    s = Solution()
    print(s.isMatch("aa", "a"))
    print(s.isMatch("aa", "a*"))
    print(s.isMatch("ab", ".*"))
    print(s.isMatch("aab", "c*a*b"))


test()