# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = ListNode()
        sum_c = sum
        c1 = l1
        c2 = l2
        prev_carry = 0

        while c1 and c2:
            res = c1.val + c2.val + prev_carry
            prev_carry = res // 10
            dig = res % 10
            sum_c.next = ListNode(dig)
            c1 = c1.next
            c2 = c2.next
            sum_c = sum_c.next
        
        #
        while c1:
            res = c1.val + prev_carry
            prev_carry = res // 10
            dig = res % 10
            sum_c.next = ListNode(dig)
            sum_c = sum_c.next
            c1 = c1.next

            # rest all the nodes of c1
            sum_c.next = c1
        
        while c2:
            res = c2.val + prev_carry
            prev_carry = res // 10
            dig = res % 10
            sum_c.next = ListNode(dig)
            sum_c = sum_c.next
            c2 = c2.next

            # rest all the nodes of c1
            sum_c.next = c2
        
        if prev_carry > 0:
            sum_c.next = ListNode(1)
        
        return sum.next




