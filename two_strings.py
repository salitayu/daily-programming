def twoStrings(s1, s2):
    substrings1 = {}
    substrings2 = {}
    for i in s1:
        substrings1[i] = substrings1.setdefault(i,0) + 1
    for i in s2:
        substrings2[i] = substrings2.setdefault(i,0) + 1
    for key in substrings1.items():
        if key in substrings2:
            return 'YES'
    return 'NO'
print(twoStrings('and', 'art'))
print(twoStrings('be', 'cat'))