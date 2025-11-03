# 数字小镇中的捣蛋鬼
from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums):
        return [k for k, v in Counter(nums).items() if v == 2]