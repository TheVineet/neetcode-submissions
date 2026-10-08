"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def bfs(node):
            q = collections.deque()
            oldToNew[node] = Node(node.val)
            q.append(node)

            while q:
                node = q.popleft()
                copy = oldToNew[node]
                for nei in node.neighbors:
                    if nei not in oldToNew:
                        oldToNew[nei] = Node(nei.val)
                        q.append(nei)
                    copy.neighbors.append(oldToNew[nei])

        if not node:
            return None
        else:
            bfs(node)
        
        return oldToNew[node]



