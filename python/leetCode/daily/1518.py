# 换水问题
class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        if numBottles < numExchange:
            return numBottles
        else:
            empty_bottle = numBottles
        all = numBottles

        while empty_bottle >= numExchange:
            all += empty_bottle // numExchange
            empty_bottle = empty_bottle % numExchange + empty_bottle // numExchange

        return all

def test():
    s = Solution()
    print(s.numWaterBottles(9, 3))
    print(s.numWaterBottles(15, 4))

test()