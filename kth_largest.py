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

# priority queue
def findKthLargest2(nums, k):
    p = []
    for i in range(len(nums)):
        heapq.heappush(p, nums[i])
        if len(p) > k:
            heapq.heappop(p)
    return p[0]

# quickselect algorithm
def findKthLargest3(nums, k):
    k = len(nums) - k
    def quickSelect(l,r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p > k:
            return quickSelect(l, p - 1)
        elif p < k:
            return quickSelect(p+1, r)
        else:
            return nums[p]
    return quickSelect(0, len(nums) - 1)

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest3(nums, k))
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest3(nums, k))
