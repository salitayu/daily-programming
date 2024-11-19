def addBoldTag(s, d):
    st = [False] * len(s)
    final = ''
    for word in d:
        start = s.find(word)
        end = len(word)
        while start != -1:
            for i in range(start, start + end):
                st[i] = True
            start = s.find(word, start+1)
    i = 0
    while i < len(s):
        if st[i]:
            final += '<b>'
            while i < len(s) and st[i]:
                final += s[i]
                i += 1
            final += '</b>'
        else:
            final += s[i]
            i += 1
    return final

print(addBoldTag('abcxyz123', ['cxy', 'xyz123']))

def addBoldTag(s, d):
    st = [False] * len(s)
    final = ''
    for word in d:
        start = s.find(word)
        end = len(word)
        while start != -1:
            for i in range(start, start + end):
                st[i] = True
            start = s.find(word, start + 1)
    i = 0
    while i < len(s):
        if st[i]:
            final += '<b>'
            while i < len(s) and st[i]:
                final += s[i]
                i += 1
            final += '</b>'
        else:
            final += s[i]
            i += 1
    return final

def addBoldTag(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: str
    """
    n = len(s)
    bold = [False] * n
    for word in words:
        start = s.find(word)
        while start != -1:
            for i in range(start, start + len(word)):
                bold[i] = True
            start = s.find(word, start + 1)
    open = '<b>'
    close = '</b>'
    ans = []
    for i in range(n):
        if bold[i] and (i == 0 or not bold[i-1]):
            ans.append(open)
        ans.append(s[i])
        if bold[i] and (i == n - 1 or not bold[i+1]):
            ans.append(close)
    return ''.join(ans)