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