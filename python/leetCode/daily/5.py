# 最长回文子串
class Solution:
    def longestPalindrome(self, s):
        l = len(s)
        if l <= 1:
            return s

        dp = [[False] * l for _ in range(l)]
        for i in range(l):
            dp[i][i] = True

        for i in range(l-1, -1, -1):
            for j in range(i+1, l):
                if j - i >= 2 and dp[i+1][j-1] and s[j] == s[i]:
                    dp[i][j] = True
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = True

        begin = 0
        max_long = 0

        for i in range(l):
            for j in range(i, l):
                if dp[i][j] and j - i + 1 > max_long:
                    max_long = j - i + 1
                    begin = i

        print(dp)
        return s[begin: begin+max_long]



def test():
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("ac"))
    print(s.longestPalindrome("aaaa"))

test()