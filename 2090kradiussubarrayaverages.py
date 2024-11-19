def kradiussubarrayaverages(nums, k):
    left = 0
    curWinSum = 0
    diameter = 2 * k + 1
    result = [-1] * len(nums)
    for right in range(0, len(nums)):
        curWinSum += nums[right]
        if right - left + 1 >= diameter:
            result[left + k] = curWinSum // diameter
            curWinSum -= nums[left]
            left += 1
    return result
