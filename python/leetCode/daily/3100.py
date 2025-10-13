# 换水问题 Ⅱ
class Solution:
    def maxBottlesDrunk(self, numBottles, numExchange):
        if numBottles < numExchange:
            return numBottles
        else:
            all = numBottles
            empty_bottle = numBottles

        while empty_bottle >= numExchange:
            all += 1
            empty_bottle = empty_bottle - numExchange + 1
            numExchange += 1

        return all
