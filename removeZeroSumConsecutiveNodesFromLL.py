class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head):
        front = ListNode(0, head)
        current = front
        prefixsum = 0
        prefixsumtonode = {}
        while current is not None:
            prefixsum += current.val
            if prefixsum in prefixsumtonode:
                prev = prefixsumtonode[prefixsum]
                current = prev.next
                p = prefixsum + current.val
                while p != prefixsum:
                    del prefixsumtonode[p]
                    current = current.val
                    p += current.val
                prev.next = current.next
            else:
                prefixsumtonode[prefixsum] = current
            current = current.next
        return front.next