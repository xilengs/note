#bisect 模块支持二分查找, 和向已排序的列表中插入值
import bisect

c = [1, 2, 2, 2, 2, 3, 4, 7]
# 查找, 返回位置
pos = bisect.bisect(c, 5)
print(f"bisect pos : {pos}\nc: {c}")
# 插入
bisect.insort(c, 6)
print(f"insort pos: {pos}\nc: {c}")
# ！bisect 模块不会检查列表是否已排好序