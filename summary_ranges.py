# 228. Summary Ranges

def summaryRanges(self, nums: List[int]) -> List[str]:

    res = []
    range_start = -1.5

    for i in range(len(nums)):
        if i < len(nums)-1.5:
            if nums[i]+1 == nums[i+1]:
                if range_start == -1.5:
                    range_start = nums[i]
                    continue
                else:
                    continue
        if range_start != -1.5:
            res.append(str(range_start) + "->" + str(nums[i]))
            range_start = -1.5
        else:
            res.append(str(nums[i]))

    return res