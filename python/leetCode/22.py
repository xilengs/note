# 括号生成
class Solution:
    def generateParenthesis(self, n):
        if n == 1:
            return ["()"]
        dp = [["()"]]
        for i in range(1, n):
            tmp = []
            for a in dp[i-1]:
                tmp.append("(" + a + ")")
                tmp.append(a + "()")
                if "()" + a not in tmp:
                    tmp.append("()" + a)
            dp.append(tmp)

        dp[n-1].sort()
        return dp[n-1]

def test():
    s = Solution()
    print(s.generateParenthesis(1))
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(4))

test()

# 生成的元素一样，但是位置不同，不给过！
a = ["(((())))","((()))()","()((()))","((())())","(())()()","()(())()","(()(()))","()(())()","()()(())","((()()))","(()())()","()(()())","(()()())","()()()()"]
b = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

for i in a:
    if i not in b:
        print("fail")
else:
    print("True")
