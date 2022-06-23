'''
630 Course Schedule III

There are n different online courses from 1 - n

You're given an array courses where courses[i] = [durationi, lastdayi]

ith course should be taken continuously for durationi days and must be finished before or on lastDayi

You will start on the 1st day and you cannot take two or more courses simultaneously

Return the max number of courses you can take.
'''
import heapq
def scheduleCourse(courses):
    courses.sort()
    p = []
    time = 0
    for c in courses:
        if time + c[0] <= c[1]:
            heapq.heappush(p, c[0])
            time += c[0]
        elif len(p) == 0 and p[0] > c[0]:
            time += c[0] - heapq.poll(p)
            heapq.heappush(p, c[0])
    return len(p)

courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
print(scheduleCourse(courses))
