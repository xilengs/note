#  使绳子变成彩色的最短时间
class Solution:
    def minCost(self, colors, neededTime):
        last_color = None
        answer = 0
        tmp = 0
        i = 0
        while i < len(colors):
            if colors[i] != last_color:
                last_color = colors[i]
                i += 1
                continue
            else:
                tmp = max(neededTime[i-1], neededTime[i])
                j = i + 1
                while j < len(colors) and colors[j] == last_color:
                    tmp = max(tmp, neededTime[j])
                    j += 1
                for needed in range(i - 1 , j):
                    answer += neededTime[needed]
                answer -= tmp
                i = j
        return answer