def longestPalindrome(s):
    slen = len(s)
    dp = [[0 for j in range(slen)] for i in range(slen)]
    start = 0
    maxlen = 1
    for i in range(0, len(s)):
        dp[i][i] = 1
    for i in range(0, len(s) - 1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
            start = i
            maxlen = 2
    for k in range(2, slen):
        for i in range(slen - k):
            j = i + k
            if s[i] == s[j] and dp[i+1][j-1]==1:
                dp[i][j] = 1
                start = i
                maxlen = max(j - i + 1, maxlen)
    return s[start:start+maxlen]

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
