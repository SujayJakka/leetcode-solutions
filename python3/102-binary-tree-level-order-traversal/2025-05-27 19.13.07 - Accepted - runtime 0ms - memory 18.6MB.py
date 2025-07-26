# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):

        res = []
        queue = Deque()
        queue.append(root)

        while queue:
            level_list = []
            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level_list.append(node.val)
        
            if level_list:
                res.append(level_list)
        
        return res


            