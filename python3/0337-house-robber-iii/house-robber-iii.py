# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if not root:
                return [0, 0]
            
            left_pair = helper(root.left)
            right_pair = helper(root.right)

            without_root = max(left_pair) + max(right_pair)
            with_root = root.val + left_pair[1] + right_pair[1]

            return [with_root, without_root]
        
        return max(helper(root))
        


