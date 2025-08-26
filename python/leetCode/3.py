# 给定一个字符串s，请你找出其中不含有重复字符的最长子串的长度。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        l_max = 0
        word = {}
        start = 0
        for i in range(len(s)):
            if s[i] in word:
                if word[s[i]] < start:
                    word[s[i]] = i
                    l += 1
                else:
                    l = l - (word[s[i]] - start)
                    start = word[s[i]]+1
                    word[s[i]] = i
            else:
                word[s[i]] = i
                l += 1
            l_max = max(l_max, l)

        return l_max
    
def test():
    s = Solution()
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    print(s.lengthOfLongestSubstring(s1))
    print(s.lengthOfLongestSubstring(s2))
    print(s.lengthOfLongestSubstring(s3))

test()