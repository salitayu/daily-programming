const bestTimeToBuySellStock = () => {
    let result = 0
    let minprice = prices[0]
    for (let i = 1; i < prices.length; i++) {
        const current = prices[i]
        if (current < minprice) {
            minprice = current
        }
        result = Math.max(result, current - minprice)
    }
    return result
}
def bestTimeToBuySellStock(prices):
    result = 0
    minprice = prices[0]
    for i in range(1, len(prices)):
        current = prices[i]
        if current < minprice:
            minprice = current
        result = max(result, current - minprice)
    return result