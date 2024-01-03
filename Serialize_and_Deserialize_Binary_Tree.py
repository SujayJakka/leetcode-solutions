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

        def recurseThing(node, res):
            if node is None:
                return "None,"
            
            res += (str(node.val) + ",")
            res += recurseThing(node.left, "")
            res += recurseThing(node.right, "")

            return res
        
        return recurseThing(root, "")
        

    def deserialize(self, data):

        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        myArray = data.split(",")

        def recurseThing():
            if myArray[0] == "None":
                myArray.pop(0)
                return None
            
            myNode = TreeNode(myArray.pop(0))
            myNode.left = recurseThing()
            myNode.right = recurseThing()

            return myNode
        
        return recurseThing()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
