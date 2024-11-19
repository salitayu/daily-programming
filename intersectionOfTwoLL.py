class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None
    a = headA
    b = headB
    while a is not b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a
