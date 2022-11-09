class StockSpanner(object):
    # Monotonic Increasing Stack
    # [50,45,40,35,30,46]
    # 50 1 45 1 40 1 35 1 30 1 46 1 + 1 + 1 + 1 = 5 47 5
    # [100,80,60,70,60,75,85]
    # [100 1] (pop) [80 1] [60 1] (pop) [70 1 + 1 = 2] (pop) [60 1] [75 1 + 2 + 1 = 4] [85 4 + 2 = 6]
    # next(47)
    # next element to check is 46, bc 46 is not greater than 47, keep looking
    # when answer for 46 is found, look at 30, 35, 40, 45, which is not greater than 46
    # next(46) returns 5 (that's how many days stock is less than or equal to 46)
    # it took 5 days to find price greater than 46
    # when we call next(47), use this info to our advantage. 
    # if it took 5 days to find a price greater than 46,
    # it takes at least 5 days to find price greater than 47

    def __init__(self):
        self.stack = []

    def next(self, price):
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.push([price, ans])
        return ans
        