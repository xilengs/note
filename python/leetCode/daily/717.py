# 比特与2比特字符
class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        if len(bits) == 1:
            return True
        if bits[-1] == 1:
            return False
        elif bits[-2] == 0:
            return True
        count = 0
        for i in range(len(bits)-2, -1, -1):
            if bits[i] == 1:
                count += 1
            else:
                break
        if count % 2:
            return False
        else:
            return True

def test():
    s = Solution()
    print(s.isOneBitCharacter([1, 1, 1, 0]))

test()