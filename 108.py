# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0], None, None)
        elif len(nums) == 2:
            return TreeNode(nums[1], TreeNode(nums[0], None, None), None)
        elif len(nums) == 3:
            return TreeNode(nums[1], TreeNode(nums[0], None, None), TreeNode(nums[2], None, None))
        else:
            smaller, bigger = nums[:len(nums) // 2], nums[len(nums)//2:]
            return TreeNode(smaller[-1], self.sortedArrayToBST(smaller[:-1]), self.sortedArrayToBST(bigger))
