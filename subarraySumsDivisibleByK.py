def subarraysDivByK(nums, k):
    d = { 0: 1 }
    res = 0
    prefixsum = 0
    for n in nums:
        prefixsum += n
        remainder = prefixsum % k
        res += d.setdefault(remainder, 0)
        d[remainder] += 1
    return res

def subarraysumequalsk(nums, k):
    d = { 0: 1 }
    count = 0
    currsum = 0
    for i in nums:
        currsum += i
        diff = currsum - k
        count += d.setdefault(diff, 0)
        d[currsum] = d.setdefault(currsum, 0) + 1
    return count

def printSubarraySumEqualsK(nums, k):
    d = {0: [-1]}
    sums = 0
    count = 0
    result = []
    for i in range(0, len(nums)):
        sums += nums[i]
        diff = sums - k
        if diff in d:
            count += 1
            for j in d[diff]:
                result.append([j+1,i])
        if sums in d:
            d[sums].append(i)
        else:
            d[sums] = [i]
    return result
