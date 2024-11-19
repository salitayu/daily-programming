def minimumWindowSubstring(s, t):
    if t == '':
        return ''

    req_count = {}
    window = {}

    slen = len(s)
    for i in range(0, slen):
        cur = s[i]
        if cur in req_count:
            req_count[cur] += 1
        else:
            req_count[cur] = 1
        window[cur] = 0

    current = 0
    required = len(req_count)
    left = 0
    result = []
    minlen = float('infinity')
    for right in range(0, slen):
        cur = s[right]
        if cur in t:
            if cur in window:
                window[cur] += 1
            else:
                window[cur] = 1
        if cur in req_count and window[cur] == req_count[cur]:
            current += 1
        while current == required:
            if (right - left + 1) < minlen:
                result = [left, right]
                minlen = right - left + 1
            if s[left] in t:
                window[s[left]] -= 1
            if s[left] in req_count and window[s[left]] < req_count[s[left]]:
                current -= 1
            left += 1
        left, right = result
    return minlen
