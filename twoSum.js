const twoSum = (nums, target) => {
    d = {}
    for (let i = 0; i < nums.length; i++) {
        const curr = nums[i]
        const diff = target - curr
        if (diff in d) {
            return [d[diff], i]
        }
        d[curr] = i
    }
    return [-1, -1]
}

console.log(twoSum([2, 7, 11, 15], 9))
console.log(twoSum([3, 2, 4], 6))
console.log(twoSum([3, 3], 6))
