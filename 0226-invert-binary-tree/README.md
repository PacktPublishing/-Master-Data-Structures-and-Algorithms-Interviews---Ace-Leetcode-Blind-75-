# Invert Binary Tree (Leetcode #226)

Binary trees are a fundamental data structure in computer science, used in a wide range of applications from databases to network routing. One common problem that helps deepen understanding of binary tree manipulation is the 'Invert Binary Tree' problem. Inverting a binary tree involves swapping all left and right children nodes to produce a mirror image of the original tree. This guide will walk you through the problem statement, a brute-force solution, an efficient approach using recursion, and an analysis of the time and space complexity involved.

## Understanding the Problem Statement

The 'Invert Binary Tree' is a common LeetCode problem that asks you to invert a given binary tree, meaning you swap all the left and right children nodes throughout the entire tree. This problem is similar to producing a mirror image of the binary tree.

The input will be the root of the binary tree, and the expected output is the root of the newly inverted tree. For example:

* Input Tree:
    

```python
    4
   / \
  2   7
 / \ / \
1  3 6  9
```

* Output Tree (after inversion):
    

```python
    4
   / \
  7   2
 / \ / \
9  6 3  1
```

The goal is to efficiently reverse the given binary tree's structure.

## Brute Force Approach

A simple brute-force approach to solve this problem could involve manually traversing the entire binary tree, swapping each left and right child node at each level, starting from the root node and moving all the way down to the leaves.

This can be achieved using a queue to perform a level-order traversal (BFS) where we swap each child node at every level.

Pseudo-code for brute-force:

* Use a queue to start from the root.
    
* Traverse each node level by level.
    
* For each node, swap its left and right child nodes.
    

While this approach is straightforward, it is not the most efficient as it requires extra memory to store the nodes for traversal.

## Hint to Solve the Problem Efficiently

The key to solving this problem efficiently lies in recursion. Think of it this way: the process of inverting a binary tree can be broken down into smaller subproblems of inverting the left and right subtrees. Once those subtrees are inverted, you simply swap them.

## Efficient Solution

The provided code offers an elegant solution using recursion to invert the binary tree.

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        # Swap the left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

Let's break down the code:

* **Base Case**: If the `root` is `None`, return `None`. This ensures that the function stops at the leaf nodes and doesn't try to access non-existent child nodes.
    
* **Swapping Children**: The main action here is to swap `root.left` and `root.right`. This effectively inverts the current node.
    
* **Recursive Call**: After swapping the children of the current node, the function recursively calls itself on `root.left` and `root.right` to invert the remaining subtrees.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(n)**, where `n` is the number of nodes in the binary tree. This is because each node is visited exactly once to perform the swap.
    
* **Space Complexity**: The space complexity of this solution is **O(h)**, where `h` is the height of the binary tree. This is due to the recursive nature of the solution, which takes up space on the call stack proportional to the height of the tree. In the worst case, for a skewed tree, this could be **O(n)**, while for a balanced tree, it would be **O(log n)**.
    

## Conclusion

Inverting a binary tree is an interesting exercise that tests your ability to think recursively. The provided solution is both concise and efficient, focusing on the principle of inverting subtrees and then combining those results to achieve the overall inversion. While brute-force approaches like BFS level-order traversal can solve the problem, a recursive approach is usually more elegant and straightforward. Feel free to implement this solution and experiment with other variations to deepen your understanding of tree traversal and recursion!


README for [Invert Binary Tree (Leetcode #226)](https://blog.unwiredlearning.com/invert-binary-tree) was compiled from the Unwired Learning Blog.