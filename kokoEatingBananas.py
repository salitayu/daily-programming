def minEatingSpeed(piles, H):
    def feasible(speed):
        return sum((pile-1)/speed+1 for pile in piles) <= H
    left = 1
    right = max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left