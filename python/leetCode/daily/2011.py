# 执行操作后的变量值
class Solution:
    def finalValueAfterOperations(self, operations):
        answer = 0
        for op in operations:
            if op == '++X' or op == 'X++':
                answer += 1
            else:
                answer -= 1

        return answer
