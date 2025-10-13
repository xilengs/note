# 给你两个正整数n和x
# 返回用不同的正整数的x次幂之和组成n的方案数。返回互不相同整数[n1,n2,n3,...,nk]的集合数目，满足这些数的x次幂之和等于n
# 输入 n = 10, x = 2
# 输出 1
# 10 = 3^2 + 1^2
# 动态规划/01背包

def numberOfWays(n: int, x: int) -> int:
    max = 10**9 + 7
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(0,n+1):
            if j < i ** x:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-i**x]) % max

    return dp[n][n]

answer = numberOfWays(10, 2)
print(answer)


