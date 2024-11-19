# nums1[i] + nums1[j] > nums2[i] + nums2[j]
# nums1[i] + nums1[j] - nums1[j] - nums2[i] > nums2[i] + nums2[j] - nums2[i] + nums1[j]
# subtract nums2[i] and nums1[j] from both sides
# nums1[i] - nums2[i] > nums2[j] - nums1[j]
# nums1[i] - nums2[i] - nums2[j] + nums1[j] > nums2[j] - nums1[j] - nums2[j] + nums1[j]
# nums1[i] - nums2[i] - nums2[j] + nums1[j] > 0
# (nums1[i] - nums2[i]) + (nums1[j] - nums2[j]) > 0
def countPairs(nums1, nums2):
    left = 0
    right = len(nums1) - 1
    result = 0
    diff = [nums1[i] - nums2[i] for i in range(len(nums1))]
    diff.sort()
    while left < right:
        if diff[left] + diff[right] > 0:
            result += right - left
            right -= 1
        else:
            left += 1
    return result