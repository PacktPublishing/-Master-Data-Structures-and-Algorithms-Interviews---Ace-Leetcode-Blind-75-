# Kth Smallest Element in a BST (Leetcode #230)

Finding specific elements in a Binary Search Tree (BST) is a common problem in computer science, often used to test knowledge of tree traversal techniques and understanding of BST properties. One such problem is determining the Kth smallest element in a BST, which requires an efficient approach to ensure optimal performance. In this blog, we will discuss the problem statement, explore a brute force approach, provide a hint for a more efficient solution, and then walk through an efficient solution with detailed time and space complexity analysis.

## Understanding the Problem Statement

The problem asks us to find the Kth smallest element in a Binary Search Tree (BST). A BST is a binary tree in which each node follows a specific order: the value of every node in the left subtree is smaller than the value of the root node, and the value of every node in the right subtree is greater. Given a BST and a value K, we need to find the value of the Kth smallest node in this tree.

For example, if the tree is:

```python
      3
     / \
    1   4
     \
      2
```

And `k = 1`, the answer is `1` because `1` is the smallest element in the tree.

## Brute Force Approach

A common brute force approach to solve this problem involves performing an in-order traversal of the BST and storing all the nodes' values in an array. In-order traversal of a BST results in the values being stored in a sorted order, which makes it easy to access the Kth smallest element. Once we have this sorted list, we simply return the K-1 indexed value from the list.

The brute force approach involves the following steps:

1. Perform an in-order traversal to store all the nodes in a list.
    
2. Retrieve the Kth smallest element by accessing the K-1 index.
    

However, this approach has a time complexity of O(N), where N is the number of nodes in the tree, and a space complexity of O(N) as well, due to storing all the nodes in an array.

## Hint to Solve the Problem Efficiently

Instead of storing all the values in an array, you can optimize the space usage by only keeping track of the count and stopping once you reach the Kth smallest element during the traversal. This eliminates the need for an entire array to store all the nodes.

## Efficient Solution

The provided code follows the brute force approach by performing an in-order traversal and storing the nodes' values in an array. Here is the given solution:

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # List to store the values of nodes in in-order traversal
        io_list = []
        
        # Populate the io_list with the in-order traversal of the tree
        self.helper(root, io_list)

        return io_list[k-1]

    def helper(self, tree_node, io_list):
        # Base case: if the node is None, return
        if tree_node is None:
            return

        self.helper(tree_node.left, io_list)
        io_list.append(tree_node.val)
        self.helper(tree_node.right, io_list)
```

In this solution, the helper function performs an in-order traversal, and all the node values are stored in the `io_list`. After completing the traversal, we simply return the `k-1` element from the list, which represents the Kth smallest element.

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(N)**, where `N` is the number of nodes in the BST. This is because we visit each node exactly once during the in-order traversal.
    
* **Space Complexity**: The space complexity is also **O(N)** due to the use of the `io_list` to store all node values. Additionally, the recursion stack space can take up to O(H), where `H` is the height of the tree, which in the worst case (skewed tree) could be O(N).
    

For an optimized solution, we could modify the in-order traversal to stop once we find the Kth element, thereby reducing the space complexity.

## Conclusion

Finding the Kth smallest element in a BST is a fundamental problem that helps to strengthen understanding of tree traversal and BST properties. While the brute force approach is straightforward, it is not the most efficient in terms of space usage. By optimizing the traversal process, we can achieve a more space-efficient solution. Understanding the trade-offs between time and space complexity is crucial when choosing the best approach for solving such problems. We hope this guide has helped you understand both the brute force and efficient ways to solve the Kth smallest element problem in a BST.


README for [Kth Smallest Element in a BST (Leetcode #230)](https://blog.unwiredlearning.com/kth-smallest-element-in-a-bst) was compiled from the Unwired Learning Blog.