
def binary_to_decimal(n):

    res = 0
    pointer = 0

    nums = list(str(n))
    
    for i in range(len(nums)):
        if nums.pop() == "1":
            res += 2**pointer
        pointer += 1

    return res


if __name__ == "__main__":
    print(binary_to_decimal(1111))
