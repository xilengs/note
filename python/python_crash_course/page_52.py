# 4.3
import time

for i in range(1, 21):
    print(i)

# 4.4
nums = [num for num in range(1, 1000001)]
"""
for num in nums:
    print(num)
"""

# 4.5
print(f"min_nums={min(nums)}, max_nums={max(nums)}")
start = time.time()
print(f"sum_nums={sum(nums)}")
end = time.time()
print(f"sum_nums use {end - start:.4f} sec")

# 4.6
odds = [num for num in range(1, 20 ,2)]
for odd in odds:
    print(odd)

# 4.7
mult_3s = [num for num in range(3, 31, 3)]
for mult_3 in mult_3s:
    print(mult_3)

#4.8 & 4.9
cube_in_ten = [num ** 3 for num in range(1, 11)]
for num in cube_in_ten:
    print(num)

# 复制列表
cube_1 = cube_in_ten
cube_2 = cube_in_ten[:]
cube_1.append(-1)
cube_2.append(-2)
cube_in_ten.append(-3)
print(cube_1)
print(cube_2)
print(cube_in_ten)

