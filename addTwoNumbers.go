package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	results := &ListNode{}
	resultref := results
	carry := 0
	for l1 != nil || l2 != nil {
		x := 0
		y := 0
		if l1 != nil {
			x = l1.Val
		}
		if l2 != nil {
			y = l2.Val
		}
		temp := x + y + carry
		resultref.Next = &ListNode{temp % 10, nil}
		resultref = resultref.Next
		carry = temp / 10
		if carry > 0 {
			resultref.Next = &ListNode{carry, nil}
		}
		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
	}
	return results.Next
}
