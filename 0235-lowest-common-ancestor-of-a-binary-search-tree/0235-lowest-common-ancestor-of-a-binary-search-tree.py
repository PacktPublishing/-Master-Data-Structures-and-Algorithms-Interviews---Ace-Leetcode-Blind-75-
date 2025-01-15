# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            
            # If both p and q are greater than root, go to right subtree
            if p.val > root.val and q.val > root.val:
                root = root.right
            
            # If both p and q are lesser than root, go to left subtree
            elif p.val < root.val and q.val < root.val:
                root = root.left
            
            else:
                # We have found the split point, i.e. the LCA node.
                return root


#Question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
#Blog: https://blog.unwiredlearning.com/lowest-common-ancestor-of-a-binary-search-tree