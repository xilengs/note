# python里的堆
# 堆在python的heapq里实现的是最小堆，核心规则只有一条：
# 父节点的值 <= 子节点的值
# 堆里最小的元素永远在索引0处

# 加入新元素时：
# 1.先放到数组末尾(树的最底层，最右边的位置)
# 2. 往上调整(sift-up):如果比父节点小，就和父节点交换，知道不再违反堆规则
import heapq

# 常用heapq操作
nums = [7, 2, 5, 3, 9]
heapq.heapify(nums)     # 建堆
print(nums)

heapq.heappush(nums, 1)     # 入堆
print(nums)

print(heapq.heappop(nums))      # 出堆(返回最小元素)
print(nums)

print(heapq.nsmallest(3, nums)) # 返回最小的n个元素
print(heapq.nlargest(2, nums))  # 返回最大的n个元素

# heapreplace():
# 弹出堆里最小的元素，然后把一个新元素压入堆中
# 一部完成，比先heappop再heappush更高效
smallest = heapq.heapreplace(nums, 10)
print('被替换的元素:', smallest)
print('新堆：', nums)