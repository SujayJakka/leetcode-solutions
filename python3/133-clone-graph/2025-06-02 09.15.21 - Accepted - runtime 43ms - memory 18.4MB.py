"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return

        old_to_new = {}
        queue = Deque([node])
        old_to_new[node.val] = Node(node.val)

        while queue:
            original_node = queue.popleft()
            cloned_node = old_to_new[original_node.val]

            if original_node.neighbors:
                for neighbor in original_node.neighbors:
                    if neighbor.val not in old_to_new:
                        new_clone = Node(neighbor.val)
                        old_to_new[neighbor.val] = new_clone
                        queue.append(neighbor)

                    cloned_node.neighbors.append(old_to_new[neighbor.val])
                    
        return old_to_new[node.val]
        