# 给你一个 m x n 的二进制矩阵 mat ，请你返回有多少个子矩形的元素全部都是 1 。
class Solution:
    def numSubmat(self, mat) -> int:
        row, col = len(mat), len(mat[0])
        print(f"Matrix size: {row}x{col}")
        ans = 0
        matrix = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i][j - 1] + 1 if j > 0 else 1
                    for k in range(i, -1, -1):
                        if matrix[k][j] == 0:
                            break
                        rowns = min(matrix[k][j], rowns)
                        ans += rowns
        return ans

s = Solution()
mat = [[1,0,1],[1,1,0],[1,1,0]]
print(s.numSubmat(mat))  # Output: 13