# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same_tree(p, q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
            else:
                return False
        

        if is_same_tree(root, subRoot):
            return True
        elif root:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False








