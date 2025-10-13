# 知道秘密的人数
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        l = [0] * n 
        l[0] = 1
        for i in range(1, delay):
            l[i] = l[i-1]
        
        for i in range(delay, forget):
            l[i] = (l[i-delay] + l[i-1]) % MOD
        
        for i in range(forget, n):
            for j in range(i-forget+1,i):
                l[j] = l[j] - l[i-forget]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            l[i] = (l[i-1]+ l[i-delay]) % MOD

        return l[n-1]

def test():
    s = Solution()
    print(s.peopleAwareOfSecret(6, 2, 4))
    print(s.peopleAwareOfSecret(4, 1, 3))

test()
        