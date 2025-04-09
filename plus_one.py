# 66. Plus One

def plusOne(self, digits: List[int]) -> List[int]:
        
    num = "".join(map(str, digits))
    
    num = list(str(int(num) + 1))

    return [int(i) for i in num]