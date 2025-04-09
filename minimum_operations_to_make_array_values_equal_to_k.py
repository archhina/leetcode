# 3375. Minimum Operations to Make Array Values Equal to K
# Distinct integers in Array larger than K

def minOperations(self, nums: List[int], k: int) -> int:
    if k > min(nums):
        return -1

    nums = set(nums)
    l = len(nums)

    if k in nums:
        return l-1
    else:
        return l