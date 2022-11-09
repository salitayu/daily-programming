/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
 var findMedianSortedArrays = function(nums1, nums2) {
    if (nums1.length + nums2.length == 1) {
        return nums1.length == 1 ? nums1[0] : nums2[0];
    }
    if (nums1.length > nums2.length) {
        return findMedian(nums2, nums1);
    } else {
        return findMedian(nums1, nums2);
    }
};
var findMedian = function(nums1, nums2) {
    var x = nums1.length;
    var y = nums2.length;
    var low = 0;
    var high = x;
    while(low <= high) {
        var partitionX = parseInt((low + high) / 2);
        var partitionY = parseInt((x + y + 1) / 2 - partitionX);
        var maxLeftX = (nums1[partitionX - 1] ? nums1[partitionX - 1] : Number.MIN_SAFE_INTEGER);
        var maxLeftY = (nums2[partitionY - 1] ? nums2[partitionY - 1] : Number.MIN_SAFE_INTEGER);
        var minRightX = (nums1[partitionX] ? nums1[partitionX] : Number.MAX_SAFE_INTEGER);
        var minRightY = (nums2[partitionY] ? nums2[partitionY] : Number.MAX_SAFE_INTEGER);
        if(maxLeftX <= minRightY && minRightX >= maxLeftY) {
            if((x + y) % 2 == 0) {
                return (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
            } else {
                console.log(maxLeftX);
                console.log(maxLeftY);
                return Math.max(maxLeftX, maxLeftY);
            }
        }
        else if(maxLeftX > minRightY) {
            high = partitionX - 1;
        } else {
            low = partitionX + 1;
        }
    }
    return 0;
};