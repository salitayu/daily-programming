def check_possibility(nums):
    err = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            if err or (i > 1 and i < len(nums) - 1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
                return False
            err = 1
    return True

print(check_possibility([4,2,3]))
print(check_possibility([4,2,1]))
print(check_possibility([3,4,2,3]))