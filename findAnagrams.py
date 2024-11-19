def findAnagrams(s, p):
    plen = len(p)
    result = []
    dicts = {}
    for char in p:
        if char in dicts:
            dicts[char] += 1
        else:
            dicts[char] = 1
    count = len(dicts)
    left = 0
    for right, char in enumerate(s):
        if char in dicts:
            dicts[char] -= 1
            if dicts[char] == 0:
                count -= 1
        if right - left + 1 == plen:
            if count == 0:
                result.append(left)
            if s[left] in dicts:
                if dicts[s[left]] == 0:
                    count += 1
                dicts[s[left]] += 1
            left += 1
    return result