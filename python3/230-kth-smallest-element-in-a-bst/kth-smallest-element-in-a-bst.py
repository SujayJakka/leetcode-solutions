# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = root.val
        cnt = k
        
        def helper(node):
            if not node:
                return
            
            nonlocal cnt, res
            
            helper(node.left)

            cnt -= 1

            if cnt == 0:
                res = node.val
                return
            
            helper(node.right)
            return
        
        helper(root)
        return res

