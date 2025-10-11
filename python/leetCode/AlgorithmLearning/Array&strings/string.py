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
                if len(strs[j]) <= j or strs[j][i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans