# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def delete(node, key):

            if not node:
                return

            if node.val == key:
                if node.left and node.right:
                    curr = node.left
                    while curr.right:
                        curr = curr.right
                    curr.right = node.right
                    return node.left
                elif node.left:
                    return node.left
                else:
                    return node.right
            else:
                if node.val > key:
                    node.left = delete(node.left, key)
                else:
                    node.right = delete(node.right, key)
                return node
        
        return delete(root, key)