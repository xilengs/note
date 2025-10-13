class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_has = [[False] * 9 for _ in range(9)]  # row_has[i][x] 表示 i 行是否有数字 x
        col_has = [[False] * 9 for _ in range(9)]  # col_has[j][x] 表示 j 列是否有数字 x
        sub_box_has = [[[False] * 9 for _ in range(3)] for _ in range(3)]  # sub_box_has[i'][j'][x] 表示 (i',j') 宫是否有数字 x

        for i, row in enumerate(board):
            for j, b in enumerate(row):
                if b == '.':
                    continue
                x = int(b) - 1  # 字符 '1'~'9' 转成数字 0~8
                if row_has[i][x] or col_has[j][x] or sub_box_has[i // 3][j // 3][x]:  # 重复遇到数字 x
                    return False
                # 标记行、列、宫包含数字 x
                row_has[i][x] = col_has[j][x] = sub_box_has[i // 3][j // 3][x] = True

        return True
