def maximumSumSubarrayOfSizeK(s, k):
    result = 0
    temp = []
    for i in range(0, len(s)):
        cur = s[i]
        if len(temp) < k:
            temp.append(cur)
        if len(temp) == k:
            tempsum = sum(temp)
            if tempsum > result:
                result = tempsum
            temp = temp[1:]
    return result

def maxSum(arr, k):
    n = len(arr)
    if n < k:
        return -1
    result = 0
    for i in range(0, k):
        result += arr[i]
    curr_sum = result
    for i in range(k, n):
        curr_sum += arr[i] - arr[i-k]
        result = max(curr_sum, result)
    return result

# print(maximumSumSubarrayOfSizeK([2, 1, 5, 1, 3, 2], 3))
# print(maximumSumSubarrayOfSizeK([2, 3, 4, 1, 5], 2))
print(maxSum([2, 1, 5, 1, 3, 2], 3))
print(maxSum([2, 3, 4, 1, 5], 2))