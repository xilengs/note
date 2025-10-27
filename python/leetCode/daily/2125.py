# 银行中的激光束数量
class Solution:
    def numberOfBeams(self, bank):
        last_item = 0
        sum = 0
        for i in range(len(bank)):
            count = bank[i].count('1')
            if count == 0:
                continue
            else:
                sum += last_item * count
                last_item = count

        return sum

