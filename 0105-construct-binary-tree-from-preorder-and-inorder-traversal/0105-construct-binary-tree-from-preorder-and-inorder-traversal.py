# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Create a map to efficiently find the index of any element in inorder list
        io_map = {}
        for i in range(len(inorder)):
            io_map[inorder[i]] = i

        # Call recursive helper function to build the tree
        return self.splitTree(preorder, io_map, 0, 0, len(inorder) - 1)

    def splitTree(self, preorder, io_map, rootIndex, left, right):

        # Base case: if the left index exceeds the right index, subtree is empty
        if left > right:
            return None

        # Create the root node with the current root element
        root = TreeNode(preorder[rootIndex])

        # Find the index of the root element in inorder list
        mid = io_map[preorder[rootIndex]]

        # Recursively build the left subtree
        if mid > left:
            root.left = self.splitTree(preorder, io_map, rootIndex + 1, left, mid - 1)

        # Recursively build the right subtree
        if mid < right:
            root.right = self.splitTree(preorder, io_map, rootIndex + mid - left + 1, mid + 1, right)

        return root     

#Question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
#Blog: https://blog.unwiredlearning.com/construct-binary-tree-from-preorder-and-inorder-traversal