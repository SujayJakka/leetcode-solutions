# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        res = []
        
        def pre_order(node):
            if node is None:
                return
            
            res.append(str(node.val))

            if node.left or node.right:
                res.append("(")
                pre_order(node.left)
                res.append(")")

            if node.right:
                res.append("(")
                pre_order(node.right)
                res.append(")")
        
        pre_order(root)
        return "".join(res)

