
import "math"
func getMinMax(m map[int]int) (min, max int) {
    if len(m) == 0 {
        return 0, 0
    }
    min = math.MaxInt32
    max = math.MinInt32
    
    for val := range m {
        if val < min {
            min = val
        }
        if val > max {
            max = val
        }
    }
    return
}
func continuousSubarrays(nums []int) int64 {
    frequency := make(map[int]int)
    left := 0
    count := int64(0)
    for right, number := range nums {
        frequency[number]++
        minValue, maxValue := getMinMax(frequency)
        for maxValue - minValue > 2 {
            if frequency[nums[left]]--; frequency[nums[left]] == 0 {
                delete(frequency, nums[left])
            }
            minValue, maxValue = getMinMax(frequency)
            left++
        }
        count += int64(right - left + 1)
    }
    return count
}
