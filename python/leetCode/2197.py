# 替换数组中的非互质数
# 困难题 Done！
class Solution:
    def GCD(self, x, y):
        while y:
            x, y = y, x%y
        return x

    def stack2pop(self, stack):
        while len(stack) >= 2:
            num1 = stack.pop()
            num2 = stack.pop()
            gcd = self.GCD(num1, num2)
            if gcd == 1:
                stack.append(num2)
                stack.append(num1)
                break
            else:
                stack.append(int(num1 * num2 / gcd))

    def replaceNonCoprimes(self, nums):
        if len(nums) == 1:
            return nums

        stack = [nums[0]]
        for i in range(1, len(nums)):
            tmp = stack.pop()
            gcd = self.GCD(tmp, nums[i])
            if gcd == 1:
                stack.append(tmp)
                stack.append(nums[i])
            else:
                stack.append(int(tmp * nums[i] / gcd))
                self.stack2pop(stack)

        return stack

def test():
    num1 = [6, 4, 3, 2, 7, 6, 2]
    num2 = [2, 2, 1, 1, 3, 3, 3]
    num3 = [517,11,121,517,3,51,3,1887,5]
    num4 = [287,41,49,287,899,23,23,20677,5,825]
    s = Solution()
    print(s.replaceNonCoprimes(num1))
    print(s.replaceNonCoprimes(num2))
    print(s.replaceNonCoprimes(num3))
    print(s.replaceNonCoprimes(num4))

test()