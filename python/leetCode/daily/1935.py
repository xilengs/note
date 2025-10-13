# 可以输入的最大单词数
class Solution:
    def canBeTypedWords(self, text, brokenLetters):
        words = [x for x in text.split(" ")]
        print(words)
        answer = 0
        for word in words:
            for letter in word:
                if letter in brokenLetters:
                    break
            else:
                answer += 1

        return answer

def test():
    s = Solution()
    print(s.canBeTypedWords("hello world", "ad"))
    print(s.canBeTypedWords("leet code", "lt"))
    print(s.canBeTypedWords("leet code", "e"))

test()

