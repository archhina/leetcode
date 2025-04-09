# 191. Number of 1 Bits

def hammingWeight( n: int) -> int:
        
    res = {"0":0, "1":0}
    pointer = 1
    while pointer < n:
        pointer = pointer*2
    
    while pointer >= 1:
        if n >= pointer:
            n -= pointer
            res["1"] += 1
        else:
            res["0"] += 1
        pointer /= 2

    return res["1"]

if __name__ == "__main__":
    print(hammingWeight(2147483645))