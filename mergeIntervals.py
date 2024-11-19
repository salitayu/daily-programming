def mergeIntervals(intervals):
    if len(intervals) == 0:
        return intervals
    intervals.sort(key = lambda x:x[0])
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        current = intervals[i]
        previous = result[-1]
        if current[0] > previous[1]:
            result.append(current)
        else:
            result[-1][1] = max(previous[1], current[1])
    return result

print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))
print(mergeIntervals([[1,4],[4,5]]))
