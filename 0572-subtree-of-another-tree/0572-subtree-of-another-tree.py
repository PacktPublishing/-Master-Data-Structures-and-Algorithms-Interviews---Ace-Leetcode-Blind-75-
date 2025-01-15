# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  	# Main function to check if subRoot is a subtree of root.
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        # Base case: if subRoot is None, it is a subtree.
        if subRoot is None: 
        	return True
      
      	# Base case: if root is None, subRoot can't be a subtree of root.
        if root == None and subRoot != None: 
        	return False

        # Check if the current tree is the same as subRoot.
        if self.isSameTree(root, subRoot): 
        	return True

        # Recursively check left and right subtrees.
        left_check = self.isSubtree(root.left, subRoot)
        right_check = self.isSubtree(root.right, subRoot)  

        return left_check or right_check
      

   	# Helper function to check if two trees are identical.
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None: 
        	return True
          
        if p == None or q == None or p.val != q.val: 
        	return False
        
        left_compare = self.isSameTree(p.left, q.left)
        right_compare = self.isSameTree(p.right, q.right)

        return left_compare and right_compare
      
      
#Question: https://leetcode.com/problems/subtree-of-another-tree
#Blog: https://blog.unwiredlearning.com/subtree-of-another-tree