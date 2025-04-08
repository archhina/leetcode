
def decimal_to_binary(n):

    res = []
    pointer = 1
    while pointer < n:
        pointer = pointer*2
    
    while pointer >= 1:
        if n >= pointer:
            n -= pointer
            res.append("1")
        else:
            res.append("0")
        pointer /= 2

    return "".join(res)
    


if __name__ == "__main__":
    print(decimal_to_binary(16))