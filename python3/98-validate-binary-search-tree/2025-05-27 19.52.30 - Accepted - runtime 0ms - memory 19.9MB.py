# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(left, node, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return helper(left, node.left, node.val) and helper(node.val, node.right, right)
        
        return helper(float("-inf"), root, float("inf"))




        
