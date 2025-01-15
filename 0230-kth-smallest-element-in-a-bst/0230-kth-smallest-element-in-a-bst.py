# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # List to store the values of nodes in in-order traversal
        io_list = []
        
        # Populate the io_list with the in-order traversal of the tree
        self.helper(root, io_list)

        return io_list[k-1]

    def helper(self, tree_node, io_list):
        # Base case: if the node is None, return
        if tree_node is None:
            return

        self.helper(tree_node.left, io_list)
        io_list.append(tree_node.val)
        self.helper(tree_node.right, io_list)
        

#Question: https://leetcode.com/problems/kth-smallest-element-in-a-bst
#Blog: https://blog.unwiredlearning.com/kth-smallest-element-in-a-bst