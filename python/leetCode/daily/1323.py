def maximum69Number(num: int) -> int:
    n = num
    i = 0
    flag = 0
    while n != 0:
        i = i + 1
        if n % 10 == 6:
            flag = i
        n = (n-n%10)/10
    if flag == 0:
        return num
    else:
        return num + 3 * 10 ** (flag-1)

num = 9669
print(maximum69Number(9669))