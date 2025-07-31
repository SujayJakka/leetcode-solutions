# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack, visited = [], [root], [False]

        while stack:
            curr, v = stack.pop(), visited.pop()
            if v:
                res.append(curr.val)
            elif curr:
                stack.append(curr)
                visited.append(True)
                stack.append(curr.right)
                visited.append(False)
                stack.append(curr.left)
                visited.append(False)
        
        return res


        