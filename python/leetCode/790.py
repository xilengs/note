class Solution:
    def numTilings(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2], dp[3] = 0, 1, 3, 5
        for i in range(4, n+1):
            dp[i] = dp[i-1] + 2 * dp[i-2] + 2 * dp[i-3] - 2

        return dp[n]

def test():
    s = Solution()
    print(s.numTilings(3))
    print(s.numTilings(1))