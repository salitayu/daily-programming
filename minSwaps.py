def minswaps(s):
    reds = []
    for i in range(0, len(s)):
        if s[i] == 'R':
            reds.append(i)
    left = 0
    right = len(reds) - 1
    swaps = 0
    while left < right:
        swaps += reds[right] - reds[left] - right + left
        left += 1
        right -= 1
    return -1 if swaps > 10 ** 9 else swaps
print(minswaps('WRRWWR'))
print(minswaps('WWRWWWRWR'))