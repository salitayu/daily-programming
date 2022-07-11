/*
You're given int array nums. Range of subarray of nums is difference between largest and smallest element in subarray.
Return sum of all subarray ranges of nums.
Subarray is contiguous non empty sequence of elements within array.
Topics: Array Stack Monotonic Stack
Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1, 2], range = 2 - 1 = 1
[2, 3], range = 3 - 2 = 1
[1, 2, 3], range = 3 - 1 = 2
Sum of all ranges = 0 + 0 + 0 + 1 + 1 + 2 = 4
*/
const subArrayRanges = (nums) => {
    let sum = 0
    for(let i = 0; i < nums.length; i++) {
        let max = -Infinity
        let min = Infinity
        for (let j = i; j < nums.length; j++) {
            const current = nums[j]
            max = Math.max(current, max)
            min = Math.min(current, min)
            sum += (max - min)
        }
    }
    return sum
}

console.log(subArrayRanges([1, 2, 3]))
