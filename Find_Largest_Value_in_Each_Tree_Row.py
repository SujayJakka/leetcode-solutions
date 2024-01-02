# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        nodes_arrays = []

        def recursive_method(node, level):
            if node == None:
                return
            else:
                if len(nodes_arrays) < level:
                    array = []
                    array.append(node.val)
                    nodes_arrays.append(array)
                
                else:
                    nodes_arrays[level-1].append(node.val)
            
                recursive_method(node.left, level + 1)
                recursive_method(node.right, level + 1)
        
        level = 1
        recursive_method(root, level)


        res = []

        for array in nodes_arrays:
            res.append(max(array))

        return res
