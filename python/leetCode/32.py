# 最长有效括号
class Solution:
    def longestValidParentheses(self, s):
        n = len(s)
        if n == 0:
            return 0
        dp = [(0, 0)] * (n+1)
        max_len = 0

        for i in range(1, n+1):
            if s[i-1] == "(":
                if dp[i-1][1] >= 0:
                    dp[i] = (dp[i-1][0]+1, dp[i-1][1]+1)
                else:
                    dp[i] = (1, 1)
                if dp[i][1] == 0 and dp[i][0] > max_len:
                    max_len = dp[i][0]
            else:
                dp[i] = (dp[i-1][0]+1, dp[i-1][1]-1)

        return max_len

def test():
    s = Solution()
    print(s.longestValidParentheses("(()"))
    print(s.longestValidParentheses(")()())"))
    print(s.longestValidParentheses(""))

test()
