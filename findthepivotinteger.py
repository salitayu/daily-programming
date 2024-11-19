def pivotInteger(n):
    prefixsum = 0
    for i in range(1, n + 1):
        prefixsum += i
    temp = 0
    for i in range(0, n):
        prefixsum -= i + 1
        if temp != prefixsum:
            temp += i + 1
        else:
            return i + 1
    return -1