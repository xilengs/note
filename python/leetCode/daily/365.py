# 水壶问题
import math
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        stack = [(0, 0)]
        self.seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == target or remain_y == target or remain_y + remain_x == target:
                return True
            if (remain_x, remain_y) in self.seen:
                continue
            self.seen.add((remain_x, remain_y))
            stack.append((x, remain_y))
            stack.append((remain_x, y))
            stack.append((0, remain_y))
            stack.append((remain_x, 0))
            stack.append((remain_x-min(remain_x, y-remain_y), remain_y+min(remain_x, y-remain_y)))
            stack.append((remain_x+min(remain_y, x-remain_x), remain_y-min(remain_y, x-remain_x)))
        return False

# 纯数学方式  
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0
  

s = Solution()
print(s.canMeasureWater(3,5,4))
print(s.canMeasureWater(2,6,5))
print(s.canMeasureWater(1,2,3))