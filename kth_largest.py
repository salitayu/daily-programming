'''
Given an int array nums and an int k, return the kth largest element in the array.
Note that it is kth largest eleemnt in the sorted order, not the kth distinct element.
nums = [3, 2, 1, 5, 6, 4]
nums = [1, 2, 3, 4, 5, 6]
k = 2
output = 5
array divide and conquer sorting heap priority queue quickselect
'''
import heapq

def findKthLargest1(nums, k):
    nums.sort()
    return nums[len(nums) - k]

def findKthLargest2(nums, k):
    p = []
    for i in range(len(nums)):
        heapq.heappush(p, nums[i])
        if len(p) > k:
            heapq.heappop(p)
    return p[0]

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest2(nums, k))
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest2(nums, k))
