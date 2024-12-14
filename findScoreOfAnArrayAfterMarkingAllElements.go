import (
    "fmt"
    "sort"
)
func findScore(nums []int) int64 {
  var result int64 = 0
  type ScoreIndex struct {
      index int
      value int
  }
  sortedStrings:=[]ScoreIndex{}
  for key, val := range nums {
      sortedStrings = append(sortedStrings, ScoreIndex{index:key, value: val})
  }
  sort.SliceStable(sortedStrings, func(i, j int) bool {
      return sortedStrings[i].value < sortedStrings[j].value
  })
  marked := make([]bool,len(nums))
  for i := range marked {
      marked[i] = false
  }
  for i := range nums {
      number := sortedStrings[i].value
      index := sortedStrings[i].index
      if (marked[index] == false) {
          result = result + int64(number)
          marked[index] = true
          if (index - 1 >= 0) {
              marked[index - 1] = true
          }
          if (index + 1 < len(nums)) {
              marked[index + 1] = true
          }
      }
  }
  return result
}
func main() {
  nums := [6]{2,3,5,1,3,2}
  fmt.Println(findScore(nums))
}
