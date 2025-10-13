# 从魔法师身上吸取的最大能量
class Solution:
    def maximumEnergy(self, energy, k):
        m = len(energy)
        if m == 1:
            return energy[0]

        dp = [0] * m
        max_energy = -1000
        for i in range(m-1, -1, -1):
            if i + k < m:
                dp[i] = dp[i + k] + energy[i]
            else:
                dp[i] = energy[i]
            if dp[i] > max_energy:
                max_energy = dp[i]

        return max_energy

def test():
    sol = Solution()
    print(sol.maximumEnergy([5,2,-10,-5,1], 3))
    print(sol.maximumEnergy([-2,-3,-1], 2))

test()
