# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 0
        
        # Stack of (node, depth) pairs
        stack = [(root, 1)]  

        while stack:
            node, depth = stack.pop()
            
            if node:
                max_depth = max(max_depth, depth)
                if node.left:
                    stack.append((node.left, depth + 1))                    
                if node.right:
                    stack.append((node.right, depth + 1))

        return max_depth
    

#Question: https://leetcode.com/problems/maximum-depth-of-binary-tree
#Blog: https://blog.unwiredlearning.com/maximum-depth-of-binary-tree