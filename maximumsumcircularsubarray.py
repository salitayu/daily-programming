def maxSubarraySumCircular(nums): # kadanes algorithm
    curMax = 0
    curMin = 0
    sum = 0
    maxSum = nums[0]
    minSum = nums[0]
    for num in nums:
        curMax = max(curMax, 0) + num
        curMin = min(curMin, 0) + num
        maxSum = max(maxSum, curMax)
        minSum = min(minSum, curMin)
        sum += num
    if sum == minSum:
        return maxSum
    else:
        return max(maxSum, sum - minSum)

print(maxSubarraySumCircular([1,-2,3,-2]))
print(maxSubarraySumCircular([5,-3,5]))
print(maxSubarraySumCircular([-3,-2,-3]))
