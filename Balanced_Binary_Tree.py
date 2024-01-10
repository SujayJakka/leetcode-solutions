# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def recursive_method(count, node):

            if node is None:
                return count
            
            else:
                left_count = recursive_method(count + 1, node.left)
                right_count = recursive_method(count + 1, node.right)

                if left_count == False or right_count == False:
                    return False
                
                if left_count - 1 > right_count:
                    return False

                if right_count - 1 > left_count:
                    return False

                return max(left_count, right_count)
        
        value = recursive_method(0, root)

        if value is False:
            return False
        else:
            return True
