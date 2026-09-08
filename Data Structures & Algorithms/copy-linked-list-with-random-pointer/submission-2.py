"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None: None}
        curr = head

        def get_node(node):
            if node not in old_to_new:
                old_to_new[node] = Node(0)
            return old_to_new[node]

        while curr:
            get_node(curr).val = curr.val
            get_node(curr).next = get_node(curr.next)
            get_node(curr).random = get_node(curr.random)
            curr = curr.next
        
        return old_to_new[head]
        