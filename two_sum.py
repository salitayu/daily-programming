def two_sum(nums, target):
    results = {}
    for i in range(0, len(nums)):
        current = nums[i]
        diff = target - current
        if diff in results:
            return [results[diff], i]
        results[current] = i
    return [-1,-1]

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
