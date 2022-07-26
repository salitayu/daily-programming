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