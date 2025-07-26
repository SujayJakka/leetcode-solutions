# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def recursive_method(node):

            nonlocal res

            if not node:
                return 0
            
            depth_left = recursive_method(node.left)
            depth_right = recursive_method(node.right)

            res = max(res, depth_left + depth_right)
            return max(depth_left, depth_right) + 1
        
        recursive_method(root)
        return res
        