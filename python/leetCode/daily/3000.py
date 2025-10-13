# 给你一个下标从0开始的二维整数数组dimensions。

# 对于所有下标i（0 <= i < dimensions.length），dimensions[i][0]表示矩形i的长度,而dimensions[i][1]表示矩形i的宽度。

# 返回对角线最长的矩形的面积。如果存在多个对角线长度相同的矩形，返回面积最大的矩形的面积。
class Solution:
    def areaOfMaxDiagonal(self, dimensions):
        l = 0
        area = 0
        for i in dimensions:
            if((i[0] ** 2 + i[1] ** 2) > l):
                l = i[0] ** 2 + i[1] ** 2
                area = i[0] * i[1]
            elif ((i[0] ** 2 + i[1] ** 2) == l):
                area = max(i[0] * i[1], area)
        
        return area