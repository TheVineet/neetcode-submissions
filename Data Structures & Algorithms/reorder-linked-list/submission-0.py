# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Finding the middle element
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is the mid

        # 2. Now reversing the second half
        current = slow.next
        slow.next = None
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        # prev = head of the reversed list

        # 3. Interleave Merge
        l1 = head
        l2 = prev

        while l2:
            nxt = l1.next
            l1.next = l2
            l1 = nxt

            # for l2
            nxt = l2.next
            l2.next = l1
            l2 = nxt


            

            
        



