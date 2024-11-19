"""
1. Sort the array in ascending order
2. Loop through the entire array and set up two pointers,
low and high on every iteration
3. Low is set to the current loop index + 1, and high is
set to the last index of the array
4. In an inner loop, look for values that, along with the
current element, sum up to target.
5. Calculate the sum of array elements pointed to by the
current loop index, and the low and high pointers.
6. If the sum is equal to target, return TRUE.
7. Else If the sum is greater than target, move the high
pointer backwards.
8. Else If the sum is greater than target, move the high
pointer backwards.
9. Else If the sum is less than target, move the low pointer
forwards.
10. Stop the inner loop when low reaches or crosses high.
Reset low to the current loop element +1, and reset high to
last index.
11. If after processing the entire array we dont find a
triplet that matches our requirement, return false."""

def threeSum(nums, target):
    nums.sort()
    for i in range(0, len(nums)):
        low = i + 1
        high = len(nums) - 1
        while low < high:
            temp = nums[low] + nums[i] + nums[high]
            if temp == target:
                return True
            elif temp > target:
                high -= 1
            else:
                low += 1
    return False

print(threeSum([-1, 2, 1, -4, 5, -3] , -8))