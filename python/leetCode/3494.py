class Solution:
    def minTime(self, skill, mana):
        m, n = len(mana), len(skill)
        if m == 1:
            return sum([time * mana[0] for time in skill])
        dp = [[0] * (n + 1) for _ in range(m)]
        dp[0][0] = 0
        for i in range(1, n+1):
            dp[0][i] = dp[0][i-1] + skill[i-1] * mana[0]

        for i in range(1, m):
            start = dp[i-1][n]
            for j in range(n-2, -1, -1):
                start = max(dp[i-1][j+1], start - skill[j] * mana[i])
            dp[i][0] = start
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1] + skill[j-1] * mana[i]

        return dp[m-1][n]

def test():
    s = Solution()
    print(s.minTime([1, 5, 2, 4], [5, 1, 4, 2]))
    print(s.minTime([1, 1, 1], [1, 1, 1]))
    print(s.minTime([1, 2, 3, 4], [1, 2]))

test()
