# 字符串元音游戏
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in 'aeiou' for c in s)