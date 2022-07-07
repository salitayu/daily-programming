def longestSubstring(str):
    results = {}
    start = 0
    maxlen = 0
    for end in range(0, len(str)):
        curr = str[end]
        if curr in results:
            start = max(start, results[curr] + 1)
        results[curr] = end
        maxlen = max(end - start + 1, maxlen)
    return maxlen

print(longestSubstring('abcabcbb'))
print(longestSubstring('pwwkew'))
print(longestSubstring('bbbbb'))
