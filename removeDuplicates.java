class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length == 0) {
            return 0;
        }
        if(nums.length == 1) {
            return 1;
        }
        int k = 1;
        for(int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] != nums[i-1]) {
                nums[k] = nums[i];
                k += 1;
            }
        }
        return k;
    }
}