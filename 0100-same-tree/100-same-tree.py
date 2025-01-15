# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both trees are empty
        if p == None and q == None:
            return True
        
        # Trees are not the same if either of them is empty or values are different
        if p == None or q == None or p.val != q.val:
            return False
        
        # Check recursively for left and right subtrees
        left_compare = self.isSameTree(p.left, q.left)
        right_compare = self.isSameTree(p.right, q.right)

        return left_compare and right_compare
    

#Question: https://leetcode.com/problems/same-tree
#Blog: https://blog.unwiredlearning.com/same-tree