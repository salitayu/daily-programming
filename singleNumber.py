def singleNumber(nums):
    result = 0
    for i in range(0, len(nums)):
        result ^= nums[i]
    return result
