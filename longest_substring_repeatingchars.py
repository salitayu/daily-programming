def longestSubstring(str):
    result = {}
    start = 0
    maxlen = 0
    for end in range(0, len(str)):
        current = str[end]
        if current in result:
            start = max(start + 1, result[current] + 1)
        result[current] = end
        maxlen = max(maxlen, end - start + 1)
    return maxlen

print(longestSubstring('abcabcbb'))
print(longestSubstring('pwwkew'))
print(longestSubstring('bbbbb'))
