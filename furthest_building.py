'''
You are given int array heights representing heights of buildings,
some bricks, and some ladders.

You start your journey from building 0 and move to the next building
to possibly using bricks or ladders.

While moving from building i to building i + 1 (0 indexed),
1. If the current building's height is greater than or equal to the next building's height,
use one ladder or (h[i + 1] - h[i]) bricks.
2. Return the furthest building index(0 based) you can reach if you can use the given ladders and bricks optimally.
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
'''

import heapq

def furthest_building(heights, bricks, ladders):
    p = []
    n = len(heights)
    bricksUsed = 0
    for i in range(1, n):
        diff = heights[i] - heights[i-1]
        if diff > 0:
            heapq.heappush(p, diff)
            if len(p) > ladders:
                bricksUsed += heapq.heappop(p)
            if bricksUsed > bricks:
                return i - 1
    return n - 1

print(furthest_building([4,2,7,6,9,14,12],5,1))
print(furthest_building([4,12,2,7,3,18,20,3,19],10,2))
print(furthest_building([14,3,19,3],17,0))