from collections import defaultdict
def findNonDuplicateNumberInstances(nums):
    # left = 0
    # right = len(nums) - 1
    # while left <= right:
    #     leftnum = nums[left]
    #     rightnum = nums[right]
    #     if leftnum == rightnum:
    #         nums[right] = 0
    #         right -= 1
    #     else:
    #         left += 1
    #         right -= 1
    # return nums
    # d = defaultdict(int)
    # for i in nums:
    #     d[i] += 1
    # return len(d)
    n = 1
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            nums[n] = nums[i]
            n += 1
    return n
print(findNonDuplicateNumberInstances([2, 3, 3, 3, 6, 9, 9]))