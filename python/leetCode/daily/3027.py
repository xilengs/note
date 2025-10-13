# 人员站位的方案数II
# 这和I解法一样，这也算是困难题？
class Solution:
    def numberOfPairs(self, points) -> int:
        points = sorted(points, key=lambda x: (x[0], -x[1]), reverse=True)
        print(points)
        answer = 0
        for i in range(len(points)-1):
            y_max = 10 ** 9
            for j in range(i+1, len(points)):
                if points[j][1] < y_max and points[j][1] >= points[i][1]:
                    y_max = points[j][1]
                    answer += 1
        return answer
    
def test():
    s = Solution()
    p1 = [[1,1], [2,2], [3,3]]
    p2 = [[6,2], [4,4], [2,6]]
    p3 = [[3,1], [1,3], [1,1]]
    p4 = [[0,3], [2,4], [0,6]]
    print(s.numberOfPairs(p1))
    print(s.numberOfPairs(p2))
    print(s.numberOfPairs(p3))
    print(s.numberOfPairs(p4))

test()