class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        d = {}
        for i in nums2:
            while (stack and i > stack[-1]):
                curr = stack.pop()
                d[curr] = i
            stack.append(i)
        return [d.get(i, -1) for i in nums1]