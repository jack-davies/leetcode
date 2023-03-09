# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False
        if root.left.val != root.right.val:
            return False
        return self.isSymmetric(TreeNode(0, root.left.left, root.right.right)) and self.isSymmetric(TreeNode(0, root.left.right, root.right.left))
