def numSubarraysWithSum(nums, goal):
    totalcount = 0
    currentsum = 0
    d = {}
    for i in range(0, len(nums)):
        cur = nums[i]
        currentsum += cur
        if currentsum == goal:
            totalcount += 1
        elif currentsum - goal in d:
            totalcount += d[currentsum-goal]
        d[currentsum] = d.setdefault(currentsum, 0) + 1
    return totalcount
