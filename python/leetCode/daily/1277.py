# 给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由1组成的正方形子矩阵的个数。
from charset_normalizer.utils import any_specified_encoding
from mpmath import matrix

# 首先遍历最左边和最上边，把其中为1的位置正方形长度记为1
# 然后遍历剩下位置，matrix[i][j]为1的情况下，如果对角[i-1][j-1]是正方形，则尝试扩一圈
# 成功则answer[i][j]等于answer[i-1][j-1]+1
# 否则长度为1
def countSquares(matrix) -> int:
    row = len(matrix)
    col = len(matrix[0])
    # print(row, col)
    answer = [[0 for _ in range(col)] for _ in range(row)]
    count = 0
    # print(answer)
    for i in range(row):
        if matrix[i][0] == 1:
            answer[i][0] = 1
            count += 1
    print(answer)
    for i in range(1, col):
        if matrix[0][i] == 1:
            answer[0][i] = 1
            count += 1
    print(answer)
    for i in range(1,row):
        for j in range(1,col):
            if matrix[i][j] == 1:
                flag = 1
                if answer[i-1][j-1]:
                    for r in range(1, answer[i-1][j-1]+1):
                        if not matrix[i-r][j]:
                            flag = 0
                            break
                    if flag:
                        for c in range(1, answer[i-1][j-1]+1):
                            if not matrix[i][j-c]:
                                flag = 0
                                break
                    if flag:
                        answer[i][j] = answer[i-1][j-1] + 1
                        count += answer[i][j]
                    else:
                        answer[i][j] = 1
                        count += 1
                else:
                    answer[i][j] = 1
                    count += 1
    print(answer)
    return count


# DP解法
# 核心 answer[i][j] = min(answer[i-1][j],answer[i][j-1],answer[i-1][j-1]) + 1
# 画图可能好理解一点，[i][j]位置的正方形与它上方、左方和对角的点处正方形大小有关，是它们之前最小的那个+1
def countSquares2(matrix) -> int:
    row, col = len(matrix), len(matrix[0])
    dp = [[0] * col for _ in range(row)]
    count = 0

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                count += dp[i][j]

    return count

m = [
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
]

n = [
    [1,0,1],
    [1,1,0],
    [1,1,0]
]

print(countSquares(m))
print(countSquares(n))
print(x for x in range(1,1))