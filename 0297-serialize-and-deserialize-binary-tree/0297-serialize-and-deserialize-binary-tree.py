# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ""
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("N")
        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1
        while queue:
            node = queue.pop(0)
            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


#Question: https://leetcode.com/problems/serialize-and-deserialize-binary-tree
#Blog: https://blog.unwiredlearning.com/serialize-and-deserialize-binary-tree