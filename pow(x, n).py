# 50. Pow(x, n)

def myPow(self, x: float, n: int) -> float:
        
    if x == -1 and n%2 == 0 or n == 0 or x == 1:
        return 1
    if x == -1 and n%2 != 0:
        return -1
    # check sign
    if n < 0:
        x = 1/x
        n = -n

    res = x
    i = 0

    # loop over n
    while i < ((n)-1):
        if abs(res) < 0.0000001:
            return 0
        if abs(n)-1 - i > 4:
            res *= x*x*x*x
            i += 4
        else:
            # multiply by x
            res *= x
            i += 1

    return res