func twoSum(nums []int, target int) []int {
    indexLocations := make(map[int]int)
    for i := range nums {
        current := nums[i]
        diff := target - current
        elem, ok := indexLocations[diff]
        if ok {
            return []int{elem, i}
        } else {
            indexLocations[current] = i
        }
    }
    return []int{-1, -1}
}