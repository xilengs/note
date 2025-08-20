# 统计字符串数组中出现字符串s的前缀数量
class Solution:
    def countPrefixes(self, words, s) -> int:
        count = 0
        for word in words:
            for ch1, ch2 in zip(word, s):
                if ch1 != ch2:
                    break
            else:
                if len(word) < len(s):
                    count += 1
        return count

# for...else语句
# 只要for不被break，for循环结束就会执行else语句
# 如果循环被break中断，else就不会执行

# s.startswith(word)会直接判断word是不是s的前缀