# 2873. Maximum Value of an Ordered Triplet I

def maximumTripletValue(self, nums: List[int]) -> int:
        
    res = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                res.append((nums[i] - nums[j]) * nums[k])
    
    return 0 if max(res) < 0 else max(res)