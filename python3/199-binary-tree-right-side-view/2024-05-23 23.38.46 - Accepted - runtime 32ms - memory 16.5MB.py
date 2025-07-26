# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        h_map = {}

        def recursive_method(node, depth):
            if node is None:
                return
            
            if depth not in h_map:
                h_map[depth] = node.val

            recursive_method(node.right, depth + 1)
            recursive_method(node.left, depth + 1)
        
        recursive_method(root, 0)

        res = [0] * len(h_map)
        for key in h_map:
            val = h_map[key]
            res[key] = val
        
        return res


        