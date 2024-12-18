import math
def eraseOverlapIntervals(self, intervals) -> int:
    intervals.sort(key=lambda x: x[1])
    ans = 0
    k = -math.inf
    for x, y in intervals:
        if x >= k:
            k = y
        else:
            ans += 1
    return ans