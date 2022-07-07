def longestPalindrome(s):
    c = 0
    r = 0
    t = []
    t.append('$')
    for i in range(0, len(s)):
        t.append('#')
        t.append(s[i])
    t.append('#')
    t.append('@')
    tlen = len(t)
    p = [0 for i in range(tlen)]
    print(t)
    for i in range(1, tlen-1):
        m = 2 * c - i
        if i < r:
            p[i] = min(r - i, p[m])
        while t[i+(1+p[i])] == t[i-(1+p[i])]:
            p[i] = p[i] + 1
        if i + p[i] > r:
            c = i
            r = i + p[i]
    maxlen = max(p)
    index = p.index(maxlen)
    result = ""
    for i in range(index - maxlen, index + maxlen):
        print(i)
        if t[i] != "$" and t[i] != "#" and t[i] != "@":
            result += t[i]
    return result

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
