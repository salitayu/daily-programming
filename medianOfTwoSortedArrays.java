class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if(nums1.length > nums2.length) {
            return findMedian(nums2, nums1);
        }
        return findMedian(nums1, nums2);
    }
    public double findMedian(int[] nums1, int[] nums2) {
        int start = 0;
        int end = nums1.length;
        while (start <= end) {
            int x = nums1.length;
            int y = nums2.length;
            int partitionx = (start + end)/2;
            int partitiony = (x + y + 1)/2 - partitionx;
            int maxLeftX = Integer.MIN_VALUE;
            int maxLeftY = Integer.MIN_VALUE;
            int minRightX = Integer.MAX_VALUE;
            int minRightY = Integer.MAX_VALUE;
            if (partitionx > 0) {
                maxLeftX = nums1[partitionx - 1];
            }
            if (partitiony > 0) {
                maxLeftY = nums2[partitiony - 1];
            }
            if (partitionx < x) {
                minRightX = nums1[partitionx];
            }
            if (partitiony < y) {
                minRightY = nums2[partitiony];
            }
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                if((x + y) % 2 == 0) {
                    return (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2.0;
                } else {
                    return Math.max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                end = partitionx - 1;
            } else {
                start = partitionx + 1;
            }
        }
        return 0.0;
    }
}