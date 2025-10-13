#给你一个二维二进制数组grid。请你找出一个边在水平方向和竖直方向上、面积最小的矩形，并且满足grid中所有的1都在矩形的内部。
#返回这个矩形可能的最小面积。

# 我的想法：先从头遍历找到最高的1，再从尾遍历找到最低的1，然后再从左边遍历找到最左的1，最后从右边遍历找到最右的1
# 这样在矩阵很大时，效率会高一点
# 但是这样代码太复杂了
# 下面是一个更简洁的实现方法，直接遍历整个矩阵，找到最小和最大的行列索引，然后计算面积
# 注意：如果没有1，返回0
# 相对的，效率会很低
class Solution:
    def minimumArea(self, grid) -> int:
        min_row, max_row = len(grid), -1
        min_col, max_col = len(grid[0]), -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)
        
        if max_row == -1:
            return 0
        
        return (max_row - min_row + 1) * (max_col - min_col + 1)

def minimumAreaV1(grid):
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
    
    print(f"left = {left}, right = {right}, top = {top}, bottom = {bottom}")
    return (bottom - top + 1) * (right - left + 1)
                    
def test():
    grid = [[0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]
    solution = Solution()
    print(solution.minimumArea(grid))  # 输出 6
    print(minimumAreaV1(grid))  # 输出 6

test()