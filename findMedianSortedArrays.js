const findMedianSortedArrays = (nums1, nums2) => {
    const nums1len = nums1.length
    const nums2len = nums2.length
    if (nums1len + nums2len === 1) {
        return nums1.length === 1 ? nums1[0] : nums2[0]
    }
    if (nums1len > nums2len) {
        return findMedian(nums2, nums1)
    } else {
        return findMedian(nums1, nums2)
    }
}

const findMedian = (nums1, nums2) => {
    const x = nums1.length
    const y = nums2.length
    let low = 0
    let high = x
    while (low <= high) {
        const partitionX = parseInt((low + high) / 2)
        const partitionY = parseInt((x + y + 1) / 2 - partitionX)
        const maxLeftX = (partitionX > 0 && nums1[partitionX-1]) ? nums1[partitionX-1]:Number.MIN_SAFE_INTEGER
        const minRightX = (partitionX != x && nums1[partitionX]) ? nums1[partitionX]:Number.MAX_SAFE_INTEGER
        const maxLeftY = (partitionY > 0 && nums2[partitionY - 1] ? nums2[partitionY]:Number.MIN_SAFE_INTEGER)
        const minRightY = (partitionY != y && nums2[partitionY] ? nums2[partitionY]:Number.MAX_SAFE_INTEGER)
        if (minRightX >= maxLeftY && minRightY >= maxLeftX) {
            if ((x + y) % 2 === 0) {
                return (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2
            } else {
                return Math.max(maxLeftX, maxLeftY)
            }
        } else if (maxLeftX > minRightY) {
            high = partitionX - 1
        } else {
            low = partitionX + 1
        }
    }
}
// const nums1 = [1,3]
// const nums2 = [2]
const nums1 = [1,2]
const nums2 = [3,4]
console.log(findMedianSortedArrays(nums1, nums2))