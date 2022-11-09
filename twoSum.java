class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> indexLocations = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            int diff = target - current;
            if (indexLocations.containsKey(diff)) {
                int index = indexLocations.get(diff);
                return new int[]{index, i};
            } else {
                indexLocations.put(current, i);
            }
        }
        return new int[]{-1,-1};
    }
}