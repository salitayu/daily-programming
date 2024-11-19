def findMax(nums):
    d = {}
    neg = []
    maxint = -1
    nums.sort()
    for i in range(1, 1001):
        d[i] = -i
    for i in nums:
        if i < 0:
            neg.append(i)
        else:
            if d[i] in neg:
                maxint = max(i, maxint)
    return maxint
    # time complexity: O(N)
    # space complexity: O(N)