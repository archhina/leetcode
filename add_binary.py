# 67. Add Binary

def addBinary(a: str, b: str) -> str:

        tmp = len(a) - len(b)
        carry = 0
        res = ""

        if tmp >= 0:
            b = "0" * tmp + b
        else:
            a = "0" * -tmp + a
        
        a = list(a)
        b = list(b)

        for i in range(len(a)):
            a_pop = a.pop()
            b_pop = b.pop()
            if a_pop == "1" and b_pop == "1" and carry == 1:
                res = "1" + res
            elif a_pop == "1" and b_pop == "1":
                res = "0" + res
                carry = 1
            elif a_pop == "1" or b_pop == "1" and carry == 1:
                res = "0" + res
                carry = 0
            elif a_pop == "1" or b_pop == "1":
                res = "1" + res
            elif carry == 1:
                res = "1" + res
                carry = 0
            else:
                res = "0" + res
        
        if carry == 1:
            res = "1" + res
        
        print(res)

if __name__ == "__main__":
    addBinary("1", "0")