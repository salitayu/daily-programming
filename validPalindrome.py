def validPalindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

print(validPalindrome('racecar'))
print(validPalindrome('leetcode'))

def checkPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def validPalindromeII(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return checkPalindrome(s, i, j - 1) or checkPalindrome(s, i + 1, j)
        i += 1
        j -= 1
    return True