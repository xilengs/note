# 执行操作后字典序最小的字符串
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        vis = [False] * n
        res = s
        # 将 s 延长一倍，方便截取轮转后的字符串 t
        s = s + s
        i = 0
        while not vis[i]:
            vis[i] = True
            for j in range(10):
                k_limit = 0 if b % 2 == 0 else 9
                for k in range(k_limit + 1):
                    # 每次进行累加之前，重新截取 t
                    t = list(s[i:i + n])
                    for p in range(1, n, 2):
                        t[p] = str((int(t[p]) + j * a) % 10)
                    for p in range(0, n, 2):
                        t[p] = str((int(t[p]) + k * a) % 10)
                    t_str = ''.join(t)
                    if t_str < res:
                        res = t_str
            i = (i + b) % n
        return res
