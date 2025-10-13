# 求最长V形对角线段的长度
class Solution:
    def f(self, l, come, flag, x, y, m, n, grid, last):
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 1 or last == grid[x][y]:
            return l
        
        l1, l2 = 0, 0
        # 0: 左上，1：右上，3：左下，2右下
        last = 2 if last == 0 else 0
        if(come == 0):
            if x-1 >= 0 and y-1 >= 0:
                l1 = self.f(l+1, 0, flag, x-1, y-1, m, n, grid, last)
            else:
                l1 = l+1
            if flag and x-1 >= 0 and y+1 < n:
                l2 = self.f(l+1, 1, 0, x-1, y+1, m, n, grid, last)
        elif(come == 1):
            if x-1 >= 0 and y+1 < n:
                l1 = self.f(l+1, 1, flag, x-1, y+1, m, n, grid, last)
            else:
                l1 = l+1
            if flag and x+1 < m and y+1 < n:
                l2 = self.f(l+1, 2, 0, x+1, y+1, m, n, grid, last)
        elif(come == 3):
            if x+1 < m and y-1 >= 0:
                l1 = self.f(l+1, 3, flag, x+1, y-1, m, n, grid, last)
            else:
                l1 = l+1
            if flag and x-1 >= 0 and y-1 >= 0:
                l2 = self.f(l+1, 0, 0, x-1, y-1, m, n, grid, last)
        else:
            if x+1 < m and y+1 < n:
                l1 = self.f(l+1, 2, flag, x+1, y+1, m, n, grid, last)
            else:
                l1 = l+1
            if flag and x+1 < m and y-1 >= 0:
                l2 = self.f(l+1, 3, 0, x+1, y-1, m, n, grid, last)
        
        return max(l1, l2, l)



    def lenOfVDiagonal(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        l = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    l = max(self.f(1, 0, 1, i-1, j-1, m, n, grid, 0), self.f(1, 1, 1, i-1, j+1, m, n, grid, 0), self.f(1, 2, 1, i+1, j+1, m, n, grid, 0), self.f(1, 3, 1, i+1, j-1, m, n, grid, 0), l)
        
        return l

        
s = Solution()
grid = [
    [1,0,2],
    [0,2,0],
    [2,0,2]
]
g = [[2,2,0,2,0,2,0],[1,2,2,1,0,2,0]]
print(s.lenOfVDiagonal(grid))  # 预期最长 = 3
print(s.lenOfVDiagonal(g))