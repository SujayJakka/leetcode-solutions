# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):

        res = []
        
        def algoThing(node, key):

            if node is None:
                return 
            
            if len(res) == key:
                res.append([node.val])
            else:
                res[key].append(node.val)
            
            algoThing(node.left, key + 1)
            algoThing(node.right, key + 1)

        algoThing(root, 0)

        
        return res
            
