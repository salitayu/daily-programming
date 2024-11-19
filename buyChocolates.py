def buyChoco(prices, money):
    prices.sort()
    diff = money - prices[1] - prices[0]
    return diff if diff >= 0 else money