# 字符串
# 最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 1:
            return strs[0]
        ans = ""
        for i in range(len(strs[0])):
            for j in range(1, n):
                if len(strs[j]) <= i or strs[j][i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans

# 翻转字符串里的单词
class Solution:
    def reverseWords(self, s):
        s = s.strip()
        words = s.split()
        words.reverse()
        # "分隔符".join(可迭代对象)  以指定的分隔符将可迭代对象的元素连接起来，返回一个新的字符串
        return " ".join(words)

# 实现strStr()
class Solution:
    def strStr(self, haystack, needle):
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1