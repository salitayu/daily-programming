def numberOfBeams(bank):
    prev = 0
    ans = 0
    for i in bank:
        count = 0
        for j in i:
            if j == '1':
                count += 1
        if count > 0:
            ans += prev * count
            prev = count
    return ans