# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.isValidBST2(root, -2**31 - 1, 2**31 + 1)

    def isValidBST2(self, root, min, max) -> bool:
        
        if root.val > min and root.val < max:
            if root.right is not None and root.left is not None:
                bool1 = self.isValidBST2(root.left, min, root.val)
                bool2 = self.isValidBST2(root.right, root.val, max)

                return bool1 and bool2

            elif root.left is not None:
                return self.isValidBST2(root.left, min, root.val)
            
            elif root.right is not None:
                return self.isValidBST2(root.right, root.val, max)
            else:
                return True
        else:
            return False



           

