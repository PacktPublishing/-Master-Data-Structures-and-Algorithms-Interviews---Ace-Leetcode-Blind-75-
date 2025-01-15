# Linked List Cycle II (Leetcode #142)

Linked lists are fundamental data structures that are widely used in various computational problems. One of the interesting challenges involving linked lists is detecting if a cycle exists within the list, and if so, determining the starting point of that cycle. Leetcode's problem 142, Linked List Cycle II, is a classic problem that tests your understanding of linked lists and how to effectively solve problems related to cycles. In this blog, we will explore the problem, discuss a common brute-force approach, and then dive into an efficient solution using Floyd's Tortoise and Hare algorithm.

## Understanding the Problem Statement

Leetcode's 142. Linked List Cycle II is an interesting problem involving linked lists. The problem requires determining if a given linked list has a cycle, and if so, returning the starting node of the cycle. If no cycle exists, the function should return `None`.

To clarify, a linked list contains a cycle if some node in the list is reachable again by continuously following its next pointer. In other words, the linked list forms a loop.

**Example:**

Consider the linked list:

```python
3 -> 2 -> 0 -> -4
     ^         |
     |_________|
```

In this example, the linked list contains a cycle starting at node 2.

The task is to find and return the node at which the cycle begins.

## Brute Force Approach

A common brute-force approach to solving this problem involves using a data structure, such as a set, to keep track of all visited nodes. As you traverse through the linked list, you add each node to the set. If a node is revisited, it indicates the start of a cycle.

**Steps for Brute Force Approach:**

1. Initialize an empty set.
    
2. Traverse the linked list node by node.
    
3. For each node, check if it is already present in the set.
    
4. If found, return the current node as it is the start of the cycle.
    
5. If the traversal reaches the end without finding a cycle, return `None`.
    

While this method works, it requires `O(n)` space for storing visited nodes, making it inefficient for large linked lists.

## Hint to Solve the Problem Efficiently

The efficient solution relies on using two pointers, often referred to as the **slow** and **fast** pointers. The idea is that if there's a cycle, the slow and fast pointers will eventually meet. Once they meet, a specific technique allows us to find the exact node where the cycle begins.

To solve the problem efficiently, think of how you can leverage these two pointers to detect the cycle and then find its start without using extra space.

## Efficient Solution

The code provided implements the **Floyd's Tortoise and Hare Algorithm**, a popular cycle detection technique. Here is the breakdown of the solution:

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        # Advance both pointers at different speeds until they meet
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            # If they meet, start from the head again and move at the same speed
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow

        # If no cycle is detected, return None
        return None
```

**Explanation:**

1. **Initialization:** Start by initializing two pointers, `slow` and `fast`, both pointing to the head of the linked list.
    
2. **Cycle Detection:** Move the `slow` pointer one step at a time and the `fast` pointer two steps at a time. If there is a cycle, the `slow` and `fast` pointers will eventually meet.
    
3. **Finding the Start of the Cycle:** Once the pointers meet, reset one pointer to the head of the list. Move both pointers one step at a time until they meet again. The meeting point is the start of the cycle.
    
4. **Return Value:** If no cycle is found, return `None`.
    

## Time and Space Complexity

* **Time Complexity:** The time complexity of this solution is `O(n)`, where `n` is the number of nodes in the linked list. In the worst case, both pointers traverse the entire list.
    
* **Space Complexity:** The space complexity is `O(1)` since no extra space is used apart from the pointers.
    

This solution is optimal for the problem as it uses constant space and efficiently detects the cycle and its starting point.

## Conclusion

The efficient approach to solving Leetcode 142 relies on the Floyd's Tortoise and Hare algorithm. By using two pointers, we can detect the presence of a cycle and identify its starting node without extra memory overhead. This method is both time-efficient and space-efficient, making it a preferred solution for this problem.


README for [Linked List Cycle II (Leetcode #142)](https://blog.unwiredlearning.com/linked-list-cycle-ii) was compiled from the Unwired Learning Blog.