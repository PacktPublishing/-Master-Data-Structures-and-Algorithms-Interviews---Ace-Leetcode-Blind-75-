# Binary Tree Level Order Traversal (Leetcode #102)

The Binary Tree Level Order Traversal question is a popular problem from LeetCode that involves traversing a binary tree level by level, similar to reading a book from top to bottom, left to right. In this blog post, we will break down the question, provide a common brute-force approach, a hint, and then dive into the efficient solution according to the provided code.

## Understanding the Problem Statement

The problem is to traverse a binary tree in level order and return each level as a list of nodes. Each level should be represented in a list, and all levels should be combined into a single list of lists.

For example, consider the following binary tree:

```python
       3
      / \
     9  20
       /  \
      15   7
```

The output should be:

```python
[
  [3],
  [9, 20],
  [15, 7]
]
```

The goal is to return a nested list where each inner list represents nodes at the same level of the tree.

## Brute Force Approach

The brute-force way to solve this problem is to perform a depth-first search (DFS) and keep track of the level of each node. The idea is to use a recursive function that traverses each node, passing the level as a parameter and appending the node value to a corresponding list. However, maintaining and updating the levels in this manner can be quite cumbersome, especially for larger trees.

In DFS, managing nodes at each level explicitly and organizing them into the desired format can require additional bookkeeping, making it less efficient in terms of both runtime and space usage.

## Hint to Solve the Problem Efficiently

To solve this problem more efficiently, consider using a breadth-first search (BFS) approach. The BFS approach is particularly well-suited for level-order traversal since it processes nodes level by level, making it straightforward to organize nodes into levels as needed.

The provided solution code uses a queue to implement BFS, which allows us to efficiently traverse the tree while keeping track of the nodes at each level.

## Efficient Solution

The provided efficient solution uses a queue to achieve a level-order traversal of the binary tree. Here is a step-by-step explanation:

```python
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
```

Here’s a breakdown of how this code works:

1. **Initialization**: We initialize an empty list `result` to store the level-wise node values and a `queue` that initially contains the root node.
    
2. **Traversal**: The while loop continues as long as there are nodes in the queue. At each iteration, we determine the number of nodes at the current level (`level_size`) and initialize an empty list (`level`) to store the node values for the current level.
    
3. **Processing Each Level**: For each node at the current level, we remove the node from the queue, append its value to the `level` list, and add its left and right children (if they exist) to the queue.
    
4. **Appending Levels**: Once all nodes at the current level have been processed, we append the `level` list to `result`.
    
5. **Returning Result**: Finally, the `result` list, containing all levels, is returned.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(N)**, where **N** is the number of nodes in the binary tree. Each node is visited once, and all operations involving each node (like adding children to the queue) take constant time.
    
* **Space Complexity**: The space complexity is **O(N)**. In the worst case, the queue will contain all nodes at the current level, which can be up to **N/2** nodes for a complete binary tree, resulting in **O(N)** space usage.
    

Using a queue for BFS helps ensure that each level of the tree is processed in sequence, making this approach both efficient and easy to implement.

## Conclusion

The Binary Tree Level Order Traversal problem is an excellent example of when to use breadth-first search (BFS) for efficient tree traversal. By leveraging a queue, we can ensure that nodes are processed level by level, which makes organizing them straightforward and efficient. The provided solution is optimal in terms of both time and space complexity, making it a robust approach for level-order traversal of binary trees. Whether you're preparing for coding interviews or enhancing your problem-solving skills, understanding and implementing BFS for tree problems is a valuable technique to master.


README for [Binary Tree Level Order Traversal (Leetcode #102)](https://blog.unwiredlearning.com/binary-tree-level-order-traversal) was compiled from the Unwired Learning Blog.