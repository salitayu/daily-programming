def reverselinkedlist(head):
    p1 = None
    p2 = head
    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3