def checkMagazine(magazine, note):
    d = {}
    for i in magazine:
        d[i] = d.setdefault(i, 0) + 1
    for i in note:
        if i not in d:
            print('No')
            return
        else:
            d[i] -= 1
            if d[i] == 0:
                del d[i]
    print('Yes')

checkMagazine('give me one grand today night', 'give one grand today')
