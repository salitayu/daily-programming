class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        maxl = 0
        d = {}
        for end in range(0, len(s)):
            curr = s[end]
            if curr in d:
                start = max(start, d[curr] + 1)
            d[curr] = end 
            maxl = max(maxl, end - start + 1)
        return maxl