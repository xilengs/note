# 按对角线进行矩阵排序
class Solution:
    def sortMatrix(self, grid):
        n = len(grid)
        if n <= 1:
            return grid
        for i in range(n * 2 - 2):
            tmp = []
            x, y = (i, 0) if i < n else (0, i-n+1)
            while x < n and y < n:
                tmp.append(grid[x][y])
                x, y = x+1, y+1
            tmp.sort(reverse=(i < n-1)) 
            x, y = (i, 0) if i < n else (0, i-n+1)
            for i in tmp:
                grid[x][y] = i
                x, y = x+1, y+1
            print(grid)

        return grid

grid = [[1,7,3],[9,8,2],[4,5,6]]
s = Solution()
print(s.sortMatrix(grid))




# other python中的排序