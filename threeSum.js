const threeSum = (nums) => {
    nums.sort((a, b) => a - b)
    const result = []
    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i-1]) {
            continue
        }
        let left = i + 1
        let right = nums.length - 1
        while (left < right) {
            const temp = nums[i] + nums[left] + nums[right]
            if (temp < 0) {
                left += 1
            } else if (temp > 0) {
                right -= 1
            } else {
                result.push([nums[i], nums[left], nums[right]])
                while (left < right && nums[left] == nums[left + 1]) {
                    left += 1
                }
                while (left < right && nums[right] == nums[right - 1]) {
                    right -= 1
                }
                left += 1
                right -= 1
            }
        }
    }
    return result
}

nums = [-1,0,1,2,-1,-4]
console.log(threeSum(nums))
