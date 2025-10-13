# 给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
class Solution:
    def findDiagonalOrder(self, mat):
        m, n = len(mat), len(mat[0])
        ans = []

        for loop in range(m + n - 1):
            if loop % 2:
                x = 0 if loop < n else loop - n + 1
                y = loop if loop < n else n - 1
                while x < m and y >= 0:
                    ans.append(mat[x][y])
                    x += 1
                    y -= 1
            else:
                x = loop if loop < m else m - 1
                y = 0 if loop < m else loop - m + 1
                while x >= 0 and y < n:
                    ans.append(mat[x][y])
                    x -= 1
                    y += 1
        
        return ans

            
