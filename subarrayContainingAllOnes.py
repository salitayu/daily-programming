def subarraycontainingallones(nums):
    maxlen = 0
    count = 0
    for i in range(0, len(nums)):
        current = nums[i]
        if current != 1:
            count = 0
        else:
            count += 1
            maxlen = max(count, maxlen)
    return maxlen

nums = [1, 2, 3, 1, 1, 3, 2, 1, 1, 1, 1, 1, 3, 2, 2, 1, 1, 1]

print(subarraycontainingallones(nums))
