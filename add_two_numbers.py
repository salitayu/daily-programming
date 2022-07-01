class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    result = ListNode(0)
    resultref = result
    carry = 0
    while l1 or l2:
        x = 0
        y = 0
        if l1.val:
            x = l1.val
        if l2.val:
            y = l2.val
        temp = x + y + carry
        result.next = ListNode(temp % 10)
        result = result.next
        carry = temp // 10
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if carry > 0:
        result.next = ListNode(carry)
    return resultref.next

l1 = ListNode(0)
l11 = l1
l1.next = ListNode(2)
l1 = l1.next
l1.next = ListNode(4)
l1 = l1.next
l1.next = ListNode(3)
l1 = l1.next
l2 = ListNode(0)
l22 = l2
l2.next = ListNode(5)
l2 = l2.next
l2.next = ListNode(6)
l2 = l2.next
l2.next = ListNode(4)

result = addTwoNumbers(l11.next,l22.next)
while result:
    print(result.val)
    result = result.next

