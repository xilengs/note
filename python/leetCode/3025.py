# 人员站位的方案数I
class Solution:
    def numberOfPairs(self, points) -> int:
        points = sorted(points, key=lambda x: (x[0], -x[1]), reverse=True)
        print(points)
        answer = 0
        for i in range(len(points)):
            y_max = 51
            for j in range(i+1, len(points)):
                if points[j][1] > points[i][1] and  points[j][1] < y_max: 
                    answer += 1
                    y_max = points[j][1]
                elif points[j][1] == points[i][1]:
                    answer+=1
                    break

        return answer
    
def test():
    point2 = [[6,2], [4,4], [2,6]]
    point1 = [[1,1], [2,2], [3,3]]
    point3 = [[3,1], [1,3], [1,1]]
    point4 = [[0,0], [0,3]]
    s = Solution()
    print(s.numberOfPairs(point1))
    print(s.numberOfPairs(point2))
    print(s.numberOfPairs(point3))
    print(s.numberOfPairs(point4))

test()