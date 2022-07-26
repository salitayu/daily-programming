const kSmallestPairs = function(nums1, nums2, k) {
    const minHeap = new MinPriorityQueue({ priority: x => x[0] })
    for (let i = 0; i < nums1.length; i++) {
        const num1 = nums1[0]
        const num2 = nums2[0]
        minHeap.enqueue([num1 + num2, i, 0])
        console.log('minHeap ', minHeap)
    }
    const n = nums2.length
    const result = []
    while (k > 0 && !minHeap.isEmpty()) {
        const [sum, i1, i2] = minHeap.dequeue().element
        result.push([nums1[i1], nums2[i2]])
        if(result.length === k) {
            return result
        } if(i2 < n - 1) {
            minHeap.enqueue([nums1[i1] + nums2[i2 + 1], i1, i2 + 1])
        }
    }
    return result
}
console.log(kSmallestPairs([1,7,11],[2,4,6],3))