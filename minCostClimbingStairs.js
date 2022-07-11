const minCostClimbingStairs = (nums) => {
    const n = nums.length
    let first = nums[0]
    let second = nums[1]
    for (let i = 2; i < n; i++) {
        const current = nums[i] + Math.min(first, second)
        first = second
        second = current
    }
    return Math.min(first, second)
}

nums = [10, 15, 20]
console.log(minCostClimbingStairs(nums))
