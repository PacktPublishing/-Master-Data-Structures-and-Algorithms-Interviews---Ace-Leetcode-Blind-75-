# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        result, queue = [], [root]

      	# Continue until there are no nodes left in the queue
        while queue:
          	# Store the number of nodes at the current level
            level_size = len(queue)
            level = []
            
            # Iterate over all nodes at the current level
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result
        
        
#Question: https://leetcode.com/problems/binary-tree-level-order-traversal
#Blog: https://blog.unwiredlearning.com/binary-tree-level-order-traversal