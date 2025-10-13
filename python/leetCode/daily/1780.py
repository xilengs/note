def checkPowersOfThree(self, n: int) -> bool:
    while(n != 0):
        if n % 3 == 0:
            n /= 3
        elif (n-1) % 3 == 0:
            n =  (n-1)/3
        else:
            return False
        return True