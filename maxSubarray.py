def maxSubarray(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i-1])
        result = max(result, nums[i])
    return result
