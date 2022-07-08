const twoSum = (nums, target) => {
    const results = {}
    for (let i = 0; i < nums.length; i++) {
        const current = nums[i]
        const diff = target - current
        if (diff in results) {
            return [results[diff], i]
        }
        results[current] = i
    }
    return [-1, -1]
}

console.log(twoSum([2, 7, 11, 15], 9))
console.log(twoSum([3, 2, 4], 6))
console.log(twoSum([3, 3], 6))
