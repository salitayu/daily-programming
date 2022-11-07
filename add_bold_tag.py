from tkinter import N


def addBoldTag(s, d):
    n = len(s)
    flag = [0] * n
    cur_end = 0
    for i in range(n):
        for w in d:
            if s.startswith(w,i):
                print(s.index(w, i))
                cur_end = max(cur_end, i+len(w))
        flag[i] = i < cur_end
    print(flag)
    ans = ''
    for i in range(n):
        if flag[i] and (i == 0 or (i > 0 and not flag[i-1])):
            ans += '<b>'
        ans += s[i]
        if flag[i] and (i == n - 1 or (i < n - 1 and not flag[i+1])):
            ans += '</b>'
    return ans
    
print(addBoldTag('abcxyz123',['a','123']))
