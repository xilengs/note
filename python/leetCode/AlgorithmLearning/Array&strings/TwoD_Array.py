# 二维数组
# 旋转矩阵
# 顺时针旋转90度，等于先对角线翻转，再水平翻转
class Solution:
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

# 零矩阵
class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        row = set()
        col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        for j in col:
            for i in range(m):
                matrix[i][j] = 0

             
def test():
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s.rotate(matrix)
    print(matrix)

test()                


            

