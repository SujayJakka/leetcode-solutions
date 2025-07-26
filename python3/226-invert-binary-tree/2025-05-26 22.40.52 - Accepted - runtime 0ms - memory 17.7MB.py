# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def recursive_function(node):
            if not node:
                return
            
            node_left = recursive_function(node.left)
            node_right = recursive_function(node.right)
            node.left = node_right
            node.right = node_left
            return node
        
        return recursive_function(root)