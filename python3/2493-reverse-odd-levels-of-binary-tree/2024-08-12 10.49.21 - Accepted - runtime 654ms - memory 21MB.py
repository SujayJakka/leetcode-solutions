# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = deque()
        queue.append(root)
        level_nodes = []
        count = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)

                    if count % 2 == 0:
                        level_nodes.append(node.left.val)
                        level_nodes.append(node.right.val)
                    else:
                        node.val = level_nodes[-1]
                        level_nodes.pop()
                
                elif level_nodes:
                    node.val = level_nodes[-1]
                    level_nodes.pop()
            count += 1
        
        return root


        