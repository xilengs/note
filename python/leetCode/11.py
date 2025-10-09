# 盛水最多的容器
class Solution:
    def maxArea(self, height):
        n = len(height)
        start, end = 0, n-1
        max_water = 0
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            max_water = max(max_water, area)
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return max_water

