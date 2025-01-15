# Construct Binary Tree from Preorder and Inorder Traversal (Leetcode #105)

Reconstructing a binary tree from its traversal sequences is a common problem in computer science, particularly in the domain of tree data structures. This problem not only tests your understanding of tree traversal techniques but also challenges your ability to use recursion effectively. In this blog, we will discuss how to construct a binary tree from given preorder and inorder traversal sequences, explore a brute force approach, and then delve into a more efficient solution.

## Understanding the Problem Statement

In this problem, you are given the preorder and inorder traversal sequences of a binary tree, and your task is to reconstruct the original binary tree.

The **preorder traversal** visits nodes in the order: root, left subtree, right subtree. The **inorder traversal** visits nodes in the order: left subtree, root, right subtree. Using both of these traversals, you can determine the structure of the entire binary tree.

For instance, suppose you have the following preorder and inorder sequences:

* Preorder: `[3, 9, 20, 15, 7]`
    
* Inorder: `[9, 3, 15, 20, 7]`
    

Your task is to use these two sequences to build the binary tree from scratch.

## Brute Force Approach

A common brute force approach to solving this problem would be to first identify the root element from the preorder sequence, then locate it in the inorder sequence to divide the sequence into left and right subtrees. This process is repeated recursively to build the entire tree.

However, this approach is inefficient since every recursive call involves searching through the inorder sequence to find the root element, leading to high time complexity due to repeated linear scans. Specifically, if we denote the length of the sequences as `n`, the time complexity of this brute force approach is **O(n^2)**, which becomes infeasible for larger inputs.

## Hint to Solve the Problem Efficiently

To solve this problem efficiently, think about how you can minimize the repeated searching in the inorder sequence. By precomputing a mapping from value to index in the inorder sequence, you can reduce the time complexity of each lookup from **O(n)** to **O(1)**.

## Efficient Solution

The provided code leverages a dictionary to map each value in the inorder sequence to its index, allowing for constant-time lookups. This reduces the time complexity significantly. Below, I will walk you through the solution:

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Create a map to efficiently find the index of any element in inorder list
        io_map = {}
        for i in range(len(inorder)):
            io_map[inorder[i]] = i

        # Call recursive helper function to build the tree
        return self.splitTree(preorder, io_map, 0, 0, len(inorder) - 1)

    def splitTree(self, preorder, io_map, rootIndex, left, right):
        # Base case: if the left index exceeds the right index, subtree is empty
        if left > right:
            return None

        # Create the root node with the current root element
        root = TreeNode(preorder[rootIndex])

        # Find the index of the root element in inorder list
        mid = io_map[preorder[rootIndex]]

        # Recursively build the left subtree
        if mid > left:
            root.left = self.splitTree(preorder, io_map, rootIndex + 1, left, mid - 1)

        # Recursively build the right subtree
        if mid < right:
            root.right = self.splitTree(preorder, io_map, rootIndex + mid - left + 1, mid + 1, right)

        return root
```

**Explanation**:

1. The `buildTree` function initializes a map (`io_map`) to store the index of each element from the inorder list.
    
2. The `splitTree` function is then called recursively to construct the binary tree.
    
    * The root is created using the current element from the preorder list.
        
    * Using `io_map`, the position of this root element in the inorder list is found, which helps determine the boundaries of the left and right subtrees.
        
    * The function then recursively constructs the left and right subtrees by adjusting the preorder index and the boundaries accordingly.
        

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(n)**, where `n` is the number of nodes in the tree. This is because each node is visited once, and with the help of the dictionary (`io_map`), each lookup takes constant time.
    
* **Space Complexity**: The space complexity is **O(n)** as well. The dictionary takes **O(n)** space to store the indices of the inorder sequence, and the recursion stack may also use up to **O(n)** space in the worst case, such as when the tree is highly unbalanced.
    

## Conclusion

Reconstructing a binary tree from its preorder and inorder traversal sequences can seem challenging at first, but with an efficient approach, it becomes quite manageable. By leveraging a dictionary to avoid repeated searches in the inorder list, we achieve a significant performance boost compared to the brute force approach. This problem is an excellent example of how thoughtful data structure choices can lead to more efficient algorithms, ultimately making our solutions scalable and practical for larger inputs.


README for [Construct Binary Tree from Preorder and Inorder Traversal (Leetcode #105)](https://blog.unwiredlearning.com/construct-binary-tree-from-preorder-and-inorder-traversal) was compiled from the Unwired Learning Blog.