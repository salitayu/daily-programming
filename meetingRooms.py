def canAttendMeetings(intervals):
    if len(intervals) == 0:
        return True
    intervals.sort(key = lambda x:x[0])
    previous = intervals[0]
    for i in range(1, len(intervals)):
        current = intervals[i]
        if current[0] < previous[1]:
            return False
        previous = current
    return True

print(canAttendMeetings([[0,30],[5,10],[15,20]]))
print(canAttendMeetings([[7,10],[2,4]]))

def minMeetingRooms(intervals):
    import heapq
    if not intervals:
        return 0
    free_rooms = []
    intervals.sort(key = lambda x:x[0])
    heapq.heappush(free_rooms, intervals[0][1])
    for i in intervals[1:]:
        if free_rooms[0] <= i[0]: # if meeting end time is less than or equal to current start time
            heapq.heappop(free_rooms) # can use same meeting room
        heapq.heappush(free_rooms, i[1]) # add meeting room
    return len(free_rooms)
