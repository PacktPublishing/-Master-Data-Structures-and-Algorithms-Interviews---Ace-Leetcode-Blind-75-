# Middle of the Linked List (Leetcode #876)

Linked lists are a fundamental data structure in computer science, and understanding how to manipulate them is key for many coding problems. One common problem is finding the middle of a linked list, which has a number of practical applications. In this blog, we will explore how to solve the "876. Middle of the Linked List" problem from LeetCode, discuss both the brute force and efficient approaches, and provide a complete solution with an explanation.

## Understanding the Problem Statement

In the "Middle of the Linked List" problem, you are given a singly linked list. The goal is to return the middle node of the linked list. If there are two middle nodes (for an even number of nodes), you should return the second middle node.

For example, consider a linked list with nodes `1 → 2 → 3 → 4 → 5`. The middle node in this case is `3`, so we return that node. If the linked list was `1 → 2 → 3 → 4 → 5 → 6`, then the middle node would be `4`, since there are two middle nodes (`3` and `4`) and we need to return the second one.

## Brute Force Approach

A common brute force approach to solving this problem is to iterate through the linked list twice:

1. Traverse the entire list to count the total number of nodes.
    
2. Traverse the list again, this time stopping at the node that is at position `n/2`, where `n` is the total number of nodes.
    

While this approach works, it has a time complexity of `O(N)` due to two separate traversals of the list and a space complexity of `O(1)`. This can be inefficient when the linked list is large, as we have to traverse the list twice.

## Hint to Solve the Problem Efficiently

To solve this problem in a more efficient way, consider using two pointers to traverse the linked list. One pointer should move at twice the speed of the other. By the time the faster pointer reaches the end of the list, the slower pointer will be at the middle.

## Efficient Solution

The efficient solution makes use of a **two-pointer technique** often called the **slow and fast pointer** approach. Here is how it works:

* We initialize two pointers, `slow` and `fast`, both starting at the head of the linked list.
    
* The `fast` pointer moves two steps at a time, while the `slow` pointer moves one step at a time.
    
* When the `fast` pointer reaches the end of the list, the `slow` pointer will be at the middle.
    

Below is the code that implements this approach:

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, slow and fast, both pointing to the head of the list.
        slow, fast = head, head
        
        # Traverse the list. The loop continues as long as fast and its next node are not None.
        while fast != None and fast.next != None:
            # Move the slow pointer one step.
            slow = slow.next
            
            # Move the fast pointer two steps.
            fast = fast.next.next
        
        # By the time the loop ends, the slow pointer will be at the middle of the list.
        return slow
```

**Explanation of the Code**

* **Initialization**: Both `slow` and `fast` pointers are initialized to the head of the linked list.
    
* **Traversal**: The `while` loop continues as long as `fast` and `fast.next` are not `None`. Inside the loop, `slow` moves one step (`slow = slow.next`), while `fast` moves two steps (`fast = fast.next.next`).
    
* **Termination**: When `fast` reaches the end (`None`), `slow` will be pointing to the middle of the list, which is then returned.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is `O(N)`, where `N` is the number of nodes in the linked list. This is because we only traverse the list once, with both pointers making progress in each iteration.
    
* **Space Complexity**: The space complexity is `O(1)` since we are only using two additional pointers (`slow` and `fast`), regardless of the size of the linked list.
    

## Conclusion

Finding the middle of a linked list is a common problem that can be approached in multiple ways. The brute force approach involves traversing the list twice, which works but is not the most efficient. The slow and fast pointer technique offers an elegant and efficient solution with a time complexity of `O(N)` and a space complexity of `O(1)`. By understanding and applying this two-pointer method, you can solve this problem in a more optimal manner. This approach is a great example of how simple pointer manipulation can lead to highly efficient algorithms for linked list problems.


README for [Middle of the Linked List (Leetcode #876)](https://blog.unwiredlearning.com/middle-of-the-linked-list) was compiled from the Unwired Learning Blog.