# Linked List Cycle (Leetcode #141)

Linked lists are a fundamental data structure in computer science, often used for their dynamic memory allocation and ease of insertion and deletion. However, they come with their own set of challenges, one of which is cycle detection. In this blog, we will explore Leetcode Problem 141, **Linked List Cycle**, and discuss various approaches to solve it, including an efficient two-pointer technique.

## Understanding the Problem Statement

Leetcode Problem 141, titled **Linked List Cycle**, presents us with the task of determining whether a linked list has a cycle in it. A linked list is said to have a cycle if, at some point, a node’s `next` pointer leads back to a previously visited node, effectively creating an infinite loop.

The question provides us with the head of a singly linked list and asks if this linked list contains a cycle. If a cycle exists, we must return `true`; otherwise, return `false`.

## Brute Force Approach

One of the more intuitive ways to solve this problem is by using a **hash set**. The idea here is to traverse the linked list and store each node we visit in the hash set. If we encounter a node that we have already seen before, we know that a cycle exists. Otherwise, we continue until we reach the end of the list.

Here is a simple version of the brute force solution:

* Create an empty hash set.
    
* Traverse the linked list, storing each node in the hash set.
    
* If the node already exists in the hash set, return `true` (indicating a cycle).
    
* If the list ends, return `false` (indicating no cycle).
    

While the brute force solution works, it requires additional space proportional to the number of nodes in the linked list.

## Hint to Solve the Problem Efficiently

The provided solution uses a technique that avoids additional data structures to track nodes. Consider the idea of **using two pointers** with different speeds: one slow pointer and one fast pointer. Think about how these two pointers can help determine whether there is a cycle in the list.

## Efficient Solution

The optimal solution is known as the **Floyd's Cycle-Finding Algorithm** or the **Tortoise and Hare Algorithm**. The core idea is to use two pointers that traverse the linked list at different speeds.

Here is the efficient code solution:

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Initialize the two pointers
        slow, fast = head, head
        
        # Traverse the list with the two pointers
        while fast is not None and fast.next is not None:
            slow = slow.next  # Move the slow pointer one step
            fast = fast.next.next  # Move the fast pointer two steps
            
            # If there's a cycle, the two pointers will meet
            if slow == fast:
                return True
        
        # If the fast pointer reaches the end, there's no cycle
        return False
```

In this solution, we initialize two pointers, `slow` and `fast`, both starting at the head of the linked list. The **slow pointer** moves one step at a time, while the **fast pointer** moves two steps at a time. If there is a cycle in the linked list, eventually, the fast pointer will catch up to the slow pointer. If the fast pointer reaches the end of the list (`None`), there is no cycle.

## Time and Space Complexity

* **Time Complexity**: The time complexity of this approach is **O(n)**, where **n** is the number of nodes in the linked list. The reason is that both pointers will traverse at most the entire linked list, and in the case of a cycle, they will meet within two complete traversals of the cycle length.
    
* **Space Complexity**: The space complexity of this approach is **O(1)**, since we are not using any extra data structures to store nodes, only two pointers. This makes it significantly more space-efficient than the hash set approach.
    

## Conclusion

Leetcode 141 presents a classic problem involving linked lists and cycle detection. While a brute force approach using a hash set can solve the problem, the **Floyd's Cycle-Finding Algorithm** is a more elegant and space-efficient solution. By employing two pointers moving at different speeds, we can detect a cycle in **O(n)** time and **O(1)** space, making it an ideal choice for this problem. Understanding this algorithm helps in mastering linked list manipulations and developing efficient problem-solving skills for more advanced data structure challenges.


README for [Linked List Cycle (Leetcode #141)](https://blog.unwiredlearning.com/linked-list-cycle) was compiled from the Unwired Learning Blog.