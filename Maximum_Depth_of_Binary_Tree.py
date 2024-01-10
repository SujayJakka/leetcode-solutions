# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return 0
        depth = 0
        def recursive(root, depth):
            depth += 1
            depth1, depth2 = depth, depth
            if(root.left):
                depth1 = recursive(root.left, depth)
            if(root.right):
                depth2 = recursive(root.right, depth)
            if(depth1 > depth2):
                depth = depth1
            else:
                depth = depth2
            return depth
        depth = recursive(root, depth)
        return depth
