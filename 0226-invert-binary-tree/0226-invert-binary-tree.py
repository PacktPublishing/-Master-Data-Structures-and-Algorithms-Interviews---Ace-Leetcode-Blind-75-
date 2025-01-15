# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root is None:
            return None

        # Swap the left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    

#Question: https://leetcode.com/problems/invert-binary-tree
#Blog: https://blog.unwiredlearning.com/invert-binary-tree