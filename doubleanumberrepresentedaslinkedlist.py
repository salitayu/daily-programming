class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def doubleIt(self, head):
    reversed_list = reverse_list(head)
    carry = 0
    current, previous = reversed_list, None
    while current:
        new_value = current.val * 2 + carry
        current.val = new_value % 10
        carry = 1 if new_value > 9 else 0
        previous, current = current, current.next
    if carry:
        previous.next = ListNode(carry)
    result = self.reverse_list(reversed_list)
    return result
def reverse_list(node):
    previous, current = None, node
    while current:
        next_node = current.next
        current.next = previous
        previous, current = current, next_node