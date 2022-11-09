def longestPalindrome(s):
    if s == "" or len(s) < 1:
        return ""
    start = 0
    end = 0
    for i in range(0, len(s)):
        len1 = expand(s, i, i)
        len2 = expand(s, i, i+1)
        len3 = max(len1, len2)
        if len3 > end:
            start = i + (len3 - 1) / 2
            end = i - (len3 / 2)
    return s[start:end+1]

def expand(s, left, right):
    L = left
    R = right
    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1
    return R - L + 1
    