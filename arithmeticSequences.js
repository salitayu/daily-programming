const arithmeticSequences = (nums) => {
	let count = 0
	let currentdiff = -1
	let result = 0
	if (result.length < 3) {
		return 0
	}
	for(let i = 0; i < nums.length; i++) {
		const tempdiff = nums[i] - nums[i-1]
		if (tempdiff !== currentdiff) {
			currentdiff = tempdiff
			count = 1
		} else {
			result += count
			count += 1
		}
	}
	return result
}
def arithmeticSequences(nums):
    count = 0
    currentdiff = -1
    result = 0
    if len(result) < 3:
        return 0
    for i in range(0, len(nums)):
        if tempdiff != currentdiff:
            currentdiff = tempdiff
            count = 1
        else:
            result += count
            count += 1
    return result