def maximum69Number (num):
    """
    :type num: int
    :rtype: int
    """
    num = str(num)
    results = [int(num)]
    for i in range(0, len(num)):
        curr = num[i]
        newnum = list(num)
        if curr == '6':
            newnum[i] = '9'
            results.append(int(''.join(newnum)))
    return max(results)
    