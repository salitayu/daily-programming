class Solution:
    def peakIndexInMountainArray(self, arr):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
    