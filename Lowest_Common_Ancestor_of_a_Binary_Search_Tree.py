# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pstack = []
        qstack = []
        res = []
        thing = root
        while(thing.val != p.val):
            if(thing.val > p.val):
                pstack.append(thing)
                thing = thing.left
            else:
                pstack.append(thing)
                thing = thing.right
        pstack.append(thing)

        thing = root

        while(thing.val != q.val):
            if(thing.val > q.val):
                qstack.append(thing)
                thing = thing.left
            else:
                qstack.append(thing)
                thing = thing.right
        qstack.append(thing)

        for element in pstack:
            if element in qstack:
                res.append(element)
        return res.pop()
        


