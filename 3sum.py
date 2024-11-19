def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            twoSumII(nums, i, res)
    return res

def twoSumII(nums, i, res):
    lo, hi = i + 1, len(nums) - 1
    while lo < hi:
        sum = nums[i] + nums[lo] + nums[hi]
        if sum < 0:
            lo += 1
        elif sum > 0:
            hi -= 1
        else:
            res.append([nums[i], nums[lo], nums[hi]])
            lo += 1
            hi -= 1
            while lo < hi and nums[lo] == nums[lo - 1]:
                lo += 1

def Sum3(nums, target):
    result = []
    nums.sort()
    for i in range(0, len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[i] + nums[right]
            if sum == target:
                result.append(sum)
            elif sum > target:
                right -= 1
            else:
                left += 1
    return result

def three_sum_leetcode(nums):
    nums.sort()
    result = []
    for left in range(0, len(nums)):
        if left > 0 and nums[left] == nums[left - 1]:
            continue
        mid = left + 1
        right = len(nums) - 1
        while mid < right:
            curr_sum = nums[left] + nums[mid] + nums[right]
            if curr_sum < 0:
                mid += 1
            elif curr_sum > 0:
                right -= 1
            else:
                result.append([nums[left], nums[mid], nums[right]])
                while mid < right and nums[mid] == nums[mid + 1]:
                    mid += 1
                while right > mid and nums[right] == nums[right - 1]:
                    right -= 1
                mid += 1
                right -= 1
    return result