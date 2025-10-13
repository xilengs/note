# 移除字母异位词后的结果数组
class Solution:
    def removeAnagrams(self, words):
        ans = [words[0]]
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(words[i-1]):
                ans.append(words[i])
        return ans

def test():
    s = Solution()
    print(s.removeAnagrams(["abba","baba","bbaa","cd","cd"]))
    print(s.removeAnagrams(["a","b","c","d","e"]))

test()
        