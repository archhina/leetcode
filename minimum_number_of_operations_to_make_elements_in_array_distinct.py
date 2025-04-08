# 3396. Minimum Number of Operations to Make Elements in Array Distinct
from typing import List

def minimumOperations(nums: List[int]) -> int:
    res = 0

    while len(nums) > 0:
        nums_set = set(nums)
        if len(nums) > len(nums_set):
            if len(nums) >= 3:
                nums = nums[3:]
                res += 1
            else:
                nums = []
                res += 1
        else:
            break   
    
    return res
    




if __name__ == "__main__":
    print(minimumOperations([1,2,3,4,2,3,3,5,7]))