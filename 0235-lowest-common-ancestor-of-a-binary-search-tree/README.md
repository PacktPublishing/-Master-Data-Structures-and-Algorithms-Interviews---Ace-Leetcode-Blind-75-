# Lowest Common Ancestor of a Binary Search Tree (Leetcode #235)

Finding the Lowest Common Ancestor (LCA) in a Binary Search Tree (BST) is a fundamental problem that often appears in technical interviews and coding challenges. The LCA of two nodes `p` and `q` in a BST is defined as the deepest node that is an ancestor to both `p` and `q`. Understanding how to efficiently find the LCA is key to mastering tree-based algorithms, especially when dealing with BSTs. In this blog, we will explore both a brute force approach and an efficient solution to solve this problem.

## Understanding the Problem Statement

In this problem, we are given a Binary Search Tree (BST) and two nodes, `p` and `q`, for which we need to find their Lowest Common Ancestor (LCA). The Lowest Common Ancestor is the deepest node that has both `p` and `q` as descendants. In simpler terms, it is the node that is common to both `p` and `q` and is farthest from the root of the tree.

For example, in a BST where `p` and `q` are two different nodes, the LCA would be the first node from the root where the paths to `p` and `q` diverge.

## Brute Force Approach

A brute force approach to solve this problem involves finding the paths from the root to the nodes `p` and `q` separately. We can traverse the BST starting from the root and store the nodes visited in each path until we reach `p` or `q`. Once both paths are available, we iterate over them to find the last common node, which would be the LCA. This method works, but it requires additional space to store the paths and takes more time to identify the common ancestor, especially when the BST is large.

## Hint to Solve the Problem Efficiently

A crucial property of the BST can make the problem easier to solve without storing the paths. In a BST:

* All values in the left subtree are smaller than the root.
    
* All values in the right subtree are greater than the root.
    

This property allows us to make a single traversal from the root to find the split point where `p` and `q` diverge. This split point will be the LCA.

## Efficient Solution

Below is the efficient solution that leverages the properties of a Binary Search Tree to find the LCA in a single traversal without storing any paths:

```python
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
```

In this solution, we start at the root and iteratively move either left or right, depending on the values of `p` and `q` relative to the current node (`root`). If both `p` and `q` are greater than `root`, it means they lie in the right subtree, so we move to `root.right`. If both are smaller, we move to `root.left`. When we encounter a node that lies between `p` and `q` (or matches one of them), we have found our LCA.

## Time and Space Complexity

* **Time Complexity**: The time complexity for this solution is **O(h)**, where `h` is the height of the tree. In the worst case, this could be `O(n)` for an unbalanced tree or **O(log n)** for a balanced BST.
    
* **Space Complexity**: The space complexity is **O(1)**, as we are not using any additional data structures for storing paths or making recursive calls. Instead, the traversal is done iteratively, keeping space requirements minimal.
    

## Conclusion

The problem of finding the Lowest Common Ancestor in a BST can be solved using an efficient single traversal approach by leveraging the properties of BSTs. While the brute force approach works, it is not optimal for large trees. The efficient solution discussed in this blog provides a time-efficient and space-efficient way to determine the LCA, making it a preferred approach for solving this problem. Understanding this solution helps in strengthening one's grasp on tree traversal techniques and how to utilize BST properties effectively.


README for [Lowest Common Ancestor of a Binary Search Tree (Leetcode #235)](https://blog.unwiredlearning.com/lowest-common-ancestor-of-a-binary-search-tree) was compiled from the Unwired Learning Blog.