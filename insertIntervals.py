import bisect

def insertInterval(intervals, newInterval):
    position = bisect.bisect(intervals, newInterval)
    intervals.insert(position, newInterval)
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        previous = result[-1]
        current = intervals[i]
        if current[0] > previous[1]:
            result.append(current)
        else:
            result[-1][1] = max(previous[1], current[1])
    return result

print(insertInterval([[1,3],[6,9]], [2,5]))