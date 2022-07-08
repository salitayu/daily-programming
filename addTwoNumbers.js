class ListNode {
    constructor(val, next) {
        this.val = (val === null ? 0 : val)
        this.next = (next === null || undefined ? 0: next)
    }
}

const addTwoNumbers = (l1, l2) => {
    let result = new ListNode(0)
    let resultRef = result
    let carry = 0
    while (l1 || l2) {
        let x = 0
        let y = 0
        if (l1.val) {
            x = l1.val
        }
        if (l2.val) {
            y = l2.val
        }
        const temp = parseInt(x + y + carry)
        const tempNode = new ListNode(temp % 10)
        result.next = tempNode
        result = result.next
        carry = parseInt(temp) / 10
        if (l1) {
            l1 = l1.next
        }
        if (l2) {
            l2 = l2.next
        }
    }
    if (carry > 0) {
        result.next = new ListNode(carry)
    }
    return resultRef.next
}

l1 = new ListNode(0)
l11 = l1
l1.next = new ListNode(2)
l1 = l1.next
l1.next = new ListNode(4)
l1 = l1.next
l1.next = new ListNode(3)
l2 = new ListNode(0)
l22 = l2
l2.next = new ListNode(5)
l2 = l2.next
l2.next = new ListNode(6)
l2 = l2.next
l2.next = new ListNode(4)
answer = addTwoNumbers(l11.next, l22.next)
while (answer) {
    console.log(answer.val)
    answer = answer.next
}
