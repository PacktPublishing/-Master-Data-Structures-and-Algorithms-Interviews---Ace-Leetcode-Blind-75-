# Validate Binary Search Tree (Leetcode #98)

The "Validate Binary Search Tree" (BST) is a popular problem from Leetcode (problem #98) that often challenges developers during coding interviews. In this blog, we will cover everything you need to solve this problem, including a common brute-force approach, a hint to get you thinking in the right direction, and a more efficient solution.

## Understanding the Problem Statement

The problem asks you to determine whether a given binary tree is a valid binary search tree. A valid BST has the following properties:

* The left subtree of a node contains only nodes with values less than the node's value.
    
* The right subtree of a node contains only nodes with values greater than the node's value.
    
* Both the left and right subtrees must also be valid binary search trees.
    

The input is the root of a binary tree, and you need to return `true` if it is a valid BST and `false` otherwise. This requires you to navigate the binary tree and ensure all nodes respect the properties of a BST.

## Brute Force Approach

A simple brute-force approach to solving this problem is to perform an in-order traversal of the tree and store the values in a list. If the in-order traversal yields a sorted list with strictly increasing values, then the tree is a valid BST. This approach involves three major steps:

1. Perform an in-order traversal of the binary tree and store the values in a list.
    
2. Iterate through the list to check if the elements are sorted in strictly increasing order.
    
3. If all elements are in order, return `true`; otherwise, return `false`.
    

While this approach works, it is not the most efficient, as it requires additional memory to store the nodes' values in a list.

## Hint to Solve the Problem Efficiently

Think about the properties of a BST and how you can verify these properties while traversing the tree. Instead of storing the nodes in a list, can you maintain a boundary for each node to check whether it is valid? Consider how you might keep track of the valid range for each node as you traverse the tree.

## Efficient Solution

The provided solution uses an in-order traversal to validate the BST property. Let's break down how the code works efficiently to solve the problem.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # List to store the values of nodes in in-order traversal
        io_list = []
        
        # Populate the io_list with the in-order traversal of the tree
        self.helper(root, io_list)

        # Assume the tree is a BST initially
        is_bst = True
        # Keep track of the previous value in the in-order traversal
        prev = io_list[0]

        # Iterate through the in-order list to check if it's sorted in increasing order
        for i in range(1, len(io_list)):
            # If the current value is not greater than the previous value, it's not a BST
            if io_list[i] <= prev:
                is_bst = False
            prev = io_list[i]

        # Return the final result
        return is_bst

    def helper(self, tree_node, io_list):
        # Base case: if the node is None, return
        if tree_node is None:
            return

        # Recursive call on the left subtree
        self.helper(tree_node.left, io_list)
        # Append the current node's value to the in_order_list
        io_list.append(tree_node.val)
        # Recursive call on the right subtree
        self.helper(tree_node.right, io_list)
```

**Explanation**:

1. **In-Order Traversal**: The helper function is used to perform an in-order traversal of the tree, storing the node values in `io_list`. An in-order traversal of a BST should produce a sorted list.
    
2. **Checking BST Property**: Once we have the in-order traversal list, we iterate through it to verify that each value is greater than the previous one. If we find any value that violates this property, we conclude that the tree is not a BST.
    

This solution effectively captures the properties of a BST by leveraging in-order traversal and verifying the ordering.

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is `O(N)`, where `N` is the number of nodes in the tree. This is because we traverse all nodes in the binary tree exactly once.
    
* **Space Complexity**: The space complexity is also `O(N)` due to the storage of node values in the list `io_list`. Additionally, the recursion stack in the worst case could require `O(N)` space if the tree is unbalanced.
    

While this approach has some memory overhead, it provides a clear and simple solution to validate the BST property efficiently.

## Conclusion

The "Validate Binary Search Tree" problem is an excellent exercise for understanding the fundamental properties of binary search trees. By using an in-order traversal, you can efficiently verify whether a tree satisfies the BST property. While there are multiple ways to solve this problem, the efficient approach presented here balances clarity and simplicity, making it a reliable method for tackling BST validation. Understanding both the brute-force and optimized methods will help you be well-prepared for similar coding challenges in the future.


README for [Validate Binary Search Tree (Leetcode #98)](https://blog.unwiredlearning.com/validate-binary-search-tree) was compiled from the Unwired Learning Blog.