'''
Wiggle sequence difference between successive numbes strictly alternate between positive and negative.
Subsequence is obtained by deleting some elements possibly zero from the original sequence, leaving the remainder elements in their original order.
'''
def wiggleMaxLength(nums):
    if len(nums) < 2:
        return len(nums)
    previousdiff = nums[1] - nums[0]
    count = 2 if nums[1] - nums[0] > 0 else 1
    for i in range(2, len(nums)):
        currentdiff = nums[i] - nums[i-1]
        if (currentdiff > 0 and previousdiff < 0) or (currentdiff < 0 and previousdiff > 0):
            count += 1
            previousdiff = currentdiff
    return count

nums = [1,7,4,9,2,5]
print(wiggleMaxLength(nums)) # 6
# 6, -3, 5, -7, 3

nums = [1,17,5,10,13,15,10,5,16,8]
print(wiggleMaxLength(nums)) # 7

nums = [1,2,3,4,5,6,7,8,9]
print(wiggleMaxLength(nums)) # 2