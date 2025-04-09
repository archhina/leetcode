# 1. Two Sum

def twoSum(self, nums: List[int], target: int) -> List[int]:

    count = {}
    res = []

    for i, v in enumerate(nums):
        if (target - v) in count:
            i2 = nums.index(target - v)
            res.append(i2)
            res.append(i)
            return res
        else:
            count[v] = 1