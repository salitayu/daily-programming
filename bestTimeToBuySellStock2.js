const maxProfit = (prices) => {
    let maxprof = 0
    for (let i = 0; i < prices.length; i++) {
        if (prices[i] > prices[i-1]) {
            maxprof += prices[i] - prices[i-1]
        }
    }
    return maxprof
}

console.log(maxProfit([7,1,5,3,6,4]))
console.log(maxProfit([1,2,3,4,5]))
console.log(maxProfit([7,6,4,3,1]))

def maxprofit(prices):
    maxprof = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            maxprof += prices[i] - prices[i-1]
    return maxprof