# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self) -> None:
        self.res = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def algoThing(node):

            if not node:
                return 0
            
            l = algoThing(node.left)
            r = algoThing(node.right)

            value = max(node.val, node.val + l, node.val + r)
            both = node.val + l + r

            if both > self.res:
                self.res = both

            if value > self.res:
                self.res = value

            return value

        algoThing(root)
        return self.res
