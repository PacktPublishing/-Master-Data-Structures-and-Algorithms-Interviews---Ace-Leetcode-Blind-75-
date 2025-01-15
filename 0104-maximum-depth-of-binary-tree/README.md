# Maximum Depth of Binary Tree (Leetcode #104)

The problem of finding the "Maximum Depth of Binary Tree" is a common question in technical interviews, particularly for those involving data structures and algorithms. It tests your understanding of binary trees and the ability to implement efficient traversal techniques. In this blog post, we will explore different approaches to solve this problem, starting with a brute force method and then moving on to a more optimized solution. We will also analyze the time and space complexities involved.

## Understanding the Problem Statement

The question "Maximum Depth of Binary Tree" asks us to determine the maximum depth (or height) of a binary tree, which represents the longest path from the root node down to the farthest leaf node. A binary tree is a data structure made up of nodes, where each node has a value and at most two children: a left child and a right child.

The depth of a binary tree is defined as the number of nodes along the longest path from the root to a leaf. For example, an empty tree has a depth of 0, while a tree with just a single node has a depth of 1.

## Brute Force Approach

A common brute-force approach to solving this problem involves using recursion. We can traverse all nodes of the binary tree to find the maximum depth by recursively finding the maximum depth of the left and right subtrees, then taking the greater of the two values and adding 1 (for the current node). This approach is straightforward but not necessarily the most efficient due to potential stack overflow with deep recursion.

Here is a simple example of the brute force approach:

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

The brute force solution uses recursion to traverse all nodes, and while it works well for small trees, it can result in inefficiency and stack overflow for larger trees.

## Hint to Solve the Problem Efficiently

To solve this problem efficiently, consider using an iterative approach with a stack to perform depth-first traversal. This method can avoid the pitfalls of recursion (such as stack overflow) and can be more suitable for large trees. The solution relies on the use of a stack to keep track of nodes and their respective depths.

## Efficient Solution

The provided code employs an iterative approach using a stack to determine the maximum depth of the binary tree. This method avoids the issues of recursion depth by explicitly managing the traversal stack.

```python
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
```

In this approach, we initialize a stack with the root node and depth 1. The stack stores pairs of nodes and their respective depths. As we iterate, we pop nodes from the stack, update the maximum depth, and push the children nodes (if they exist) with incremented depth values back onto the stack. This ensures we traverse every node, updating the maximum depth as we go.

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(N)**, where **N** is the number of nodes in the binary tree. This is because we need to visit each node exactly once to determine the maximum depth.
    
* **Space Complexity**: The space complexity of the solution is **O(N)** in the worst case. In the worst-case scenario, the binary tree is completely unbalanced (i.e., all nodes are on one side), resulting in a stack that grows to **N** nodes. For a balanced tree, the space complexity would be **O(log N)** due to the height of the tree being **log N**.
    

## Conclusion

Finding the maximum depth of a binary tree is a fundamental problem that helps in understanding the basics of tree traversal. While a brute-force recursive approach can solve the problem, an iterative approach using a stack is more efficient and avoids potential pitfalls associated with recursion, especially for larger trees. By using iterative depth-first traversal, we can ensure a robust solution that handles both balanced and unbalanced trees effectively.

Understanding different methods to solve this problem provides valuable insight into tree traversal techniques and their respective advantages and trade-offs. Whether you are preparing for an interview or enhancing your problem-solving skills, mastering both approaches is essential.


README for [Maximum Depth of Binary Tree (Leetcode #104)](https://blog.unwiredlearning.com/maximum-depth-of-binary-tree) was compiled from the Unwired Learning Blog.