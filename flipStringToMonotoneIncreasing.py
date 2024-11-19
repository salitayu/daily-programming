def flipStringToMonotoneIncreasing(s):
    num = 0
    ans = 0
    for i in s:
        if i == '0':
            ans = min(ans + 1, num)
        else:
            num += 1
    return ans

flipStringToMonotoneIncreasing("00110")
