# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # List to store the values of nodes in in-order traversal
        io_list = []
        
        # Populate the io_list with the in-order traversal of the tree
        self.helper(root, io_list)

        # Assume the tree is a BST initially
        is_bst = True
        # Keep track of the previous value in the in-order traversal
        prev = io_list[0]

        # Iterate through the in-order list to check if it's sorted in increasing order
        for i in range(1, len(io_list)):
            # If the current value is not greater than the previous value, it's not a BST
            if io_list[i] <= prev:
                is_bst = False
            prev = io_list[i]

        # Return the final result
        return is_bst

    def helper(self, tree_node, io_list):
        # Base case: if the node is None, return
        if tree_node is None:
            return

        # Recursive call on the left subtree
        self.helper(tree_node.left, io_list)
        # Append the current node's value to the in_order_list
        io_list.append(tree_node.val)
        # Recursive call on the right subtree
        self.helper(tree_node.right, io_list)
        
        
#Question: https://leetcode.com/problems/validate-binary-search-tree
#Blog: https://blog.unwiredlearning.com/validate-binary-search-tree