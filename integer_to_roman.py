# 12. Integer to Roman

def intToRoman(self, num: int) -> str:
    res = []

    if num >= 1000:
        temp = int(num/1000)
        num -= 1000 * temp
        res.append("M" * temp)
    if num >= 900:
        num -= 900
        res.append("CM")
    if num >= 500:
        num -= 500
        res.append("D")
    if num >= 400:
        num -= 400
        res.append("CD")
    if num >= 100:
        temp = int(num/100)
        num -= 100 * temp
        res.append("C" * temp)
    if num >= 90:
        num -= 90
        res.append("XC")
    if num >= 50:
        num -= 50
        res.append("L")
    if num >= 40:
        num -= 40
        res.append("XL")
    if num >= 10:
        temp = int(num/10)
        num -= 10 * temp
        res.append("X" * temp)
    if num >= 9:
        num -= 9
        res.append("IX")
    if num >= 5:
        num -= 5
        res.append("V")
    if num >= 4:
        num -= 4
        res.append("IV")
    else:
        res.append("I" * num)
    return "".join(res)