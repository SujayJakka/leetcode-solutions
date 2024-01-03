# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = [0]
        
        def recursive_method(node, currMaximum):
            
            if node == None:
                return
            
            if node.val >= currMaximum:
                res[0] += 1
                currMaximum = node.val

            recursive_method(node.left, currMaximum)
            recursive_method(node.right, currMaximum)
        
            return

        recursive_method(root, float("-inf"))
        return res[0]
