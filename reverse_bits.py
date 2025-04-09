# 190. Reverse Bits

def reverseBits(n: int) -> int:

    # res = []
    # pointer = 1
    # while pointer < n:
    #     pointer = pointer*2
    
    # while pointer >= 1:
    #     if n >= pointer:
    #         n -= pointer
    #         res.append("1")
    #     else:
    #         res.append("0")
    #     pointer /= 2

    # n = "".join(res)
    # if len(n) < 32:
    #     n = "0"*(32-len(n)) + n 
    n = f"{n:032b}"



    res = 0
    pointer = 0
    nums = list(n[::-1])
    
    for i in range(len(nums)):
        if nums.pop() == "1":
            res += 2**pointer
        pointer += 1

    return res

if __name__ == "__main__":
    print(reverseBits(11111111111111111111111111111101))