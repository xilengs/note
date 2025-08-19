# 记录每一段连续零数组的长度len，在这个零数组中含一个零的子数组为len个，长度为2的子数组出现len-1个...
# 则这一段零数组出现sum(x for x in range(1, len+1))个子零数组
def zeroFilledSubarray(nums) -> int:
    answer = 0
    len = 0
    for i in nums:
        if i == 0:
            len += 1
        else:
            answer += sum(x for x in range(1, len+1))
            len = 0
    if len != 0:
        answer += sum(x for x in range(1, len+1))
    return answer

nums = [0,0,0,2,0,0]
print(zeroFilledSubarray(nums))
nums1 = [1,3,0,0,2,0,0,4]
print(zeroFilledSubarray(nums1))
nums2 = [2,10,2019]
print(zeroFilledSubarray(nums2))