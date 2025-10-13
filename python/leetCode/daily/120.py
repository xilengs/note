# 三角形最小路径和
class Solution:
    def minimumTotal(self, triangle):
        l = len(triangle)
        f = [[0] * l for _ in range(l)]
        f[0][0] = triangle[0][0]

        for i in range(1, l):
            f[i][0] = f[i-1][0] +triangle[i][0]
            for j in range(1, i):
                f[i][j] = min(f[i-1][j-1], f[i-1][j]) + triangle[i][j]
            f[i][i] = f[i-1][i-1] + triangle[i][i]

        return min(f[l-1])
