# 最大三角形面积
class Solution:
    def largestTriangleArea(self, points):
        area = 0
        n = len(points)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    s = (points[i][0] * (points[j][1] - points[k][1]) + points[j][0] * (points[k][1] - points[i][1]) + points[k][0] * (points[i][1] - points[j][1])) / 2.0
                    s = abs(s)
                    if s > area:
                        area = s

        return area

