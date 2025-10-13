# 避免洪水泛滥
import heapq
class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        ans = [-1] * n
        heap_extract = []
        last_rain = {}

        for i in range(n):
            if rains[i] > 0:
                if rains[i] in last_rain:
                    tmp = []
                    found_sunny = False
                    while heap_extract:
                        idx = heapq.heappop(heap_extract)
                        if idx > last_rain[rains[i]]:
                            ans[idx] = rains[i]
                            found_sunny = True
                            break
                        else:
                            tmp.append(idx)
                    for day in tmp:
                        heapq.heappush(heap_extract, day)
                    if not found_sunny:
                        return []
                last_rain[rains[i]] = i
            else:
                heapq.heappush(heap_extract, i)

        while heap_extract:
            idx = heapq.heappop(heap_extract)
            ans[idx] = 1


        return ans


def test():
    s = Solution()
    print(s.avoidFlood([1,2,3,4]))
    print(s.avoidFlood([1,2,0,0,2,1]))
    print(s.avoidFlood([1,2,0,1,2]))
    print(s.avoidFlood([69, 0, 0, 0, 69]))
    print(s.avoidFlood([1,0,2,0,2,1]))

test()


