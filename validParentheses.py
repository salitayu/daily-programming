def isValid(s):
    d = {")": "(", "}": "{", "]": "["}
    stack = []
    for i in s:
        if i in d:
            mappeditem = d[i]
            topitem = stack.pop() if len(stack) > 0 else ""
            if mappeditem != topitem:
                return False
            else:
                stack.append(i)
    return len(stack) == 0

def isValid1(s):
    stack = []
    opening = "{(["
    closing = "})]"
    for i in range(0, len(s)):
        cur = s[i]
        if len(stack) == 0 and cur in closing:
            return False
        elif len(stack) > 0 and cur in closing:
            if opening.index(stack[-1]) == closing.index(cur):
                stack.pop()
            else:
                return False
        else:
            stack.append(cur)
    return len(stack) == 0