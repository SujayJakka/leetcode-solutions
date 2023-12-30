"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:


    def cloneGraph(self, node: 'Node') -> 'Node':

        if node == None:
            return None

        oldToNew = {}
        queue = []
        visitedMap = {}
        queue.append(node)

        while(len(queue) > 0):
            oldNode = queue.pop(0)
            newNode = Node(oldNode.val, [])
            visitedMap[oldNode] = 1
            oldToNew[oldNode] = newNode

            for neighborNode in oldNode.neighbors:
                if neighborNode not in visitedMap:
                    queue.append(neighborNode)
            
        for oldNode in oldToNew:
            newNode = oldToNew[oldNode]

            for neighborNode in oldNode.neighbors:
                newNode.neighbors.append(oldToNew[neighborNode])
        
        return oldToNew[node]

