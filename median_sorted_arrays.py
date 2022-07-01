import sys

def findMedian(nums1, nums2):
    x = len(nums1)
    y = len(nums2)
    start = 0
    end = x
    while start <= end:
        partitionX = (start + end) // 2
        partitionY = (x + y + 1) // 2 - partitionX
        maxLeftX = nums1[partitionX - 1] if partitionX > 0 else -sys.maxsize
        maxLeftY = nums2[partitionY - 1] if partitionY > 0 else -sys.maxsize
        minRightX = nums1[partitionX] if partitionX != x else sys.maxsize
        minRightY = nums2[partitionY] if partitionY != y else sys.maxsize
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / float(2)
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            end = partitionX - 1
        else:
            start = partitionX + 1
    return 0

def findMedianSortedArrays(nums1, nums2):
    if len(nums2) < len(nums1):
        return findMedian(nums2, nums1)
    else:
        return findMedian(nums1, nums2)
