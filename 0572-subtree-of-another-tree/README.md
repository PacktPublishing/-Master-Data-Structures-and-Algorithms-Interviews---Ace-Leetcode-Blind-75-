# Subtree of Another Tree (Leetcode #572)

Binary trees are an important data structure in computer science, and they often form the basis of many interesting coding problems. One such problem is determining whether a given tree is a subtree of another tree. In this blog, we'll discuss Leetcode Problem 572: **Subtree of Another Tree**. We'll explore both the brute force approach and an efficient solution to solve this problem, using Python code to illustrate each step. Let's dive in!

## Understanding the Problem Statement

In this Leetcode problem, we are given two binary trees, **root** and **subRoot**, and we need to determine if **subRoot** is a subtree of **root**. A subtree consists of a node in the tree and all of its descendants. Essentially, the subtree must be identical to some part of the given tree. For example, if you imagine cutting off one part of a tree and seeing if it matches another smaller tree, that's what we're trying to determine here.

## Brute Force Approach

The most straightforward approach to solve this problem is to consider every node in the **root** tree and try to determine if any of these nodes are identical to the **subRoot** tree. The idea is to perform a traversal of the **root** tree and, at each step, compare the subtree starting at the current node to **subRoot**. This solution uses a **depth-first traversal** to locate nodes, and for every potential starting point, it checks if the subtree matches **subRoot**.

The brute force approach is feasible, but not very efficient since it repeatedly performs tree comparisons for each possible subtree in **root**.

## Hint to Solve the Problem Efficiently

To solve the problem efficiently, a good approach is to make use of a helper function that checks if two trees are identical. The efficient solution involves reducing the number of comparisons by combining a direct tree traversal with a subtree comparison. The idea is to avoid unnecessary work by optimizing the traversal and comparison steps.

## Efficient Solution

The efficient solution, as outlined in the provided code, leverages two functions:

1. `isSubtree(root, subRoot)` - This function checks if **subRoot** is a subtree of **root**.
    
2. `isSameTree(p, q)` - This helper function checks if two trees, **p** and **q**, are identical.
    

The core logic of `isSubtree` function includes:

1. **Base cases**: If **subRoot** is `None`, then it is automatically a subtree of **root**. If **root** is `None` but **subRoot** is not `None`, it cannot be a subtree.
    
2. **Subtree Comparison**: We use the `isSameTree` function to check if **root** and **subRoot** are identical, which means that all nodes in both trees have the same value and structure.
    
3. **Recursive Call**: If the current node of **root** does not match **subRoot**, we recursively call `isSubtree` for the left and right children of **root**.
    

Here is the Python code for reference:

```python
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if subRoot is None:
            return True
        if root == None and subRoot != None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        left_check = self.isSubtree(root.left, subRoot)
        right_check = self.isSubtree(root.right, subRoot)

        return left_check or right_check

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None or p.val != q.val:
            return False

        left_compare = self.isSameTree(p.left, q.left)
        right_compare = self.isSameTree(p.right, q.right)

        return left_compare and right_compare
```

## Time and Space Complexity

* **Time Complexity**: The time complexity of the solution is **O(m × n)**, where **m** is the number of nodes in **root** and **n** is the number of nodes in **subRoot**. In the worst case, for each node in **root**, we could potentially compare it with every node in **subRoot**.
    
* **Space Complexity**: The space complexity is **O(n)** in the worst case due to the recursion stack used by the helper function `isSameTree`, where **n** is the height of the **root** tree. The recursive calls are made for each node, resulting in a linear stack depth in the worst scenario.
    

## Conclusion

The **Subtree of Another Tree** problem is a great exercise for understanding recursive tree traversal and comparison. While the brute force approach works, the efficient solution optimizes both time and space, making use of recursive calls and base conditions effectively. By using helper functions to check if two trees are identical, we can significantly reduce unnecessary comparisons and arrive at a more elegant solution. Understanding these approaches will not only help you solve this particular problem but also enhance your ability to think recursively for similar tree-based problems.


README for [Subtree of Another Tree (Leetcode #572)](https://blog.unwiredlearning.com/subtree-of-another-tree) was compiled from the Unwired Learning Blog.