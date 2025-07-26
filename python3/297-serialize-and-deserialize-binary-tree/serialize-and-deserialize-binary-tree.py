# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        serialize_arr = []

        def pre_order(node):
            if not node:
                serialize_arr.append("N")
                return
            
            serialize_arr.append(str(node.val))
            pre_order(node.left)
            pre_order(node.right)

        pre_order(root)
        return ",".join(serialize_arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        data = data.split(",")
        counter = 0

        def pre_order():

            nonlocal counter

            if data[counter] == "N":
                counter += 1
                return
            
            root = TreeNode(int(data[counter]))
            counter += 1
            root.left = pre_order()
            root.right = pre_order()
            return root
        
        return pre_order()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))