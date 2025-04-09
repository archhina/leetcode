# 13. Roman to Integer

def romanToInt(self, s: str) -> int:
    total = 0
    i = 0

    symbols = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    

    while i < len(s):
        
        if (i < len(s) -1):
            temp = s[i] + s[i+1]
            if temp in symbols:
                total += symbols[temp]
                i += 2
                continue
        total += symbols[s[i]]
        i += 1
    return total