public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int>indexLocations = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            int current = nums[i];
            int diff = target - current;
            if (indexLocations.ContainsKey(diff)) {
                return new int[]{indexLocations[diff], i};
            } else {
                indexLocations[current] = i;
            }
        }
        return new int[]{-1,-1};
    }
}