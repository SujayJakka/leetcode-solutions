class Solution:
    def __init__(self):
        self.arrayThing = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root.left is not None:
            result = self.kthSmallest(root.left, k)
            if result is not None:
                return result

        self.arrayThing.append(root.val)

        if len(self.arrayThing) == k:
            res = self.arrayThing[k - 1]
            return res

        if root.right is not None:
            result = self.kthSmallest(root.right, k)
            if result is not None:
                return result

        return None
