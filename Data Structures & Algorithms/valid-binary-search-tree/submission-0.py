# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(curr, leftBoundary, rightBoundary):
            if not curr:
                return True
            if not (curr.val > leftBoundary and curr.val < rightBoundary):
                return False
            return (valid(curr.left, leftBoundary, curr.val) and valid(curr.right, curr.val, rightBoundary))
        
        return valid(root, float("-inf"), float("inf"))