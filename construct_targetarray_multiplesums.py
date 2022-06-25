'''
You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < n and set the value of arr at index i to x.
You may repeat this procedure as many times as needed.
Return true if it is possible to construct the target array from arr, otherwise, return false.
'''
import heapq

def isPossible(target):
    h = [-n for n in target]
    total = sum(target)
    heapq.heapify(h)
    while h[0] != -1:
        cand = -heapq.heappop(h)
        diff = total - cand
        if diff <= 0 or cand <= diff:
            return False
        prev = cand % diff
        heapq.heappush(h, -prev)
        total -= cand
        total += prev
    return True
