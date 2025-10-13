# 和为零的N个不同整数
class Solution:
    def sumZero(self, n: int):
        answer = []
        if n % 2 == 1:
            answer.append(0)
        num = int(n / 2) if n % 2 == 0 else int((n-1) / 2)
        for i in range(num):
            answer.append(i+1)
            answer.append(-i-1)

        return answer