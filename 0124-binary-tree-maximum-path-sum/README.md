# Binary Tree Maximum Path Sum (Leetcode #124)

In this blog post, we’re going to dive into a classic algorithm problem from LeetCode - "Binary Tree Maximum Path Sum." This problem challenges our understanding of tree traversal techniques and how to efficiently manage potential paths through a binary tree to achieve the maximum sum.

## Understanding the Problem Statement

The "Binary Tree Maximum Path Sum" problem involves finding the maximum path sum in a given binary tree. Here, a path is defined as any sequence of nodes starting from some node and ending at any other node along the parent-child connections. Importantly, paths don't have to pass through the root.

The task is to return the highest possible sum of node values from any such path within the given tree. For instance, if a tree contains negative values, our answer may just be a single node that holds the maximum value.

## Brute Force Approach

A brute force approach to solve this problem could involve attempting to calculate the path sum for all possible paths that exist in the tree. This could be done by considering each node as a potential "root" of a subtree and recursively finding paths through all possible combinations. This method quickly becomes inefficient as the number of nodes increases, leading to a time complexity of O(2^n) where n is the number of nodes. The overlapping subproblems, combined with recalculating the path sums again and again, make this approach impractical for large trees.

## Hint to Solve the Problem Efficiently

To solve this problem efficiently, consider employing a Depth-First Search (DFS) strategy that traverses the tree only once, while keeping track of the maximum sum encountered during this traversal. Utilize recursion to accumulate the path sum, and always return the maximum possible contribution that the current node and its subtrees can provide.

The key idea here is to consider the possibility of a "new path" starting at the current node, which could lead to a higher sum than merely continuing along an existing path. By balancing between starting new paths and continuing previous ones, you ensure that the global maximum is always updated correctly.

## Efficient Solution

The provided code leverages a DFS approach to solve the problem in an efficient manner. Here's a step-by-step breakdown of how it works:

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Recursive call on left and right child
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Update max_sum if it's better to start a new path
            price_newpath = node.val + left_gain + right_gain
            nonlocal max_sum
            max_sum = max(max_sum, price_newpath)

            # For recursion return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return max_sum
```

**Explanation**

1. **Initialization**: We define `max_sum` to keep track of the global maximum path sum encountered. Initially, it's set to negative infinity.
    
2. **DFS Function**: The `dfs(node)` function is used to traverse the binary tree recursively.
    
    * If the current node is `None`, we simply return 0 because it cannot contribute to any path sum.
        
    * We then make recursive calls for both the left and right children of the current node.
        
    * **Left and Right Gain**: We use `max(dfs(node.left), 0)` to ignore any negative contributions from the left or right subtree, thus ensuring that only positive contributions are counted.
        
3. **Calculating New Path**: At each node, we calculate the potential new path sum (`price_newpath`) by summing the value of the current node with the contributions from both left and right subtrees.
    
4. **Update Maximum Sum**: We then update the `max_sum` variable to store the highest value encountered during our traversal.
    
5. **Recursion**: The function returns the maximum gain achieved by extending either to the left or right child, helping the parent node in further calculations.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(n)**, where n is the number of nodes in the binary tree. Each node is visited exactly once, and the operations performed at each node are O(1).
    
* **Space Complexity**: The space complexity is **O(h)**, where h is the height of the tree. This is due to the recursive call stack, which can reach up to the height of the tree. In the worst case of a skewed tree, the height could be equal to the number of nodes, leading to O(n) space complexity. However, for a balanced tree, the space complexity would be O(log n).
    

The efficient solution presented here ensures that the traversal of the tree is optimal, and the algorithm effectively tracks the maximum path sum using a DFS approach with dynamic updates to the global `max_sum`.

## Conclusion

The "Binary Tree Maximum Path Sum" problem is an excellent example of how recursion and depth-first search can be used to solve complex tree traversal problems efficiently. By focusing on both local and global maximum sums during the traversal, the solution ensures that every potential path is considered. The approach discussed here avoids recalculations and minimizes time complexity, making it ideal for large binary trees. Understanding this solution helps build a strong foundation for solving other tree-related algorithmic challenges effectively.


README for [Binary Tree Maximum Path Sum (Leetcode #124)](https://blog.unwiredlearning.com/binary-tree-maximum-path-sum) was compiled from the Unwired Learning Blog.