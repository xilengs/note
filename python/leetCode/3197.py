# 给你一个二维 二进制 数组 grid。你需要找到 3 个 不重叠、面积 非零 、边在水平方向和竖直方向上的矩形，并且满足 grid 中所有的 1 都在这些矩形的内部。
# 返回这些矩形面积之和的 最小 可能值。
# 注意，这些矩形可以相接。
class Solution: 
    def minimumArea(grid):
        left, right, top, bottom = -1, -1, -1, -1
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    top = i
                    left = j
                    break
            if top != -1:
                break
        else:
            return 0
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    bottom = i
                    right = j
                    break
            if bottom != -1:
                break

        left, right = min(left, right), max(left, right)
        
        for j in range(left):
            for i in range(top, bottom + 1):
                if grid[i][j] == 1:
                    left = j
                    break
            if left == j:
                break
        
        for j in range(n-1, right, -1):
            for i in range(top, bottom + 1):
                if grid[i][j] == 1:
                    right = j
                    break
            if right == j:
                break
    
        return (bottom - top + 1) * (right - left + 1)
    
    def minimumSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        area = m * n
        # 以i划分大矩形和两个小矩形
        for i in range( m - 1):
            for j in range(n - 1):
                area = min(area, (self.minimumArea(grid[:i])+self.minimumArea(grid[i:][:j])+self.minimumArea(grid[i:][j:])), (self.minimumArea(grid[:i][:j])+self.minimumArea(grid[:i][j:])+self.minimumArea(grid[i:])) )

        # 以j划分大矩形和两个小矩形
        for j in range(n-1):
            for i in range(m-1):
                area = min(area, (self.minimumArea(grid[:][:j])+self.minimumArea(grid[:i][j:])+self.minimumArea(grid[:i][j:])), (self.minimumArea(grid[:i][:j])+self.minimumArea(grid[i:][:j])+self.minimumArea(grid[:][j:])))

        # 三条横线划分三个矩形
        for i in range(m-2):
            pass