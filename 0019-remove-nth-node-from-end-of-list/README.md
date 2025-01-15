# Remove Nth Node From End of List (Leetcode #19)

The "Remove Nth Node From End of List" problem from Leetcode is a common question in coding interviews, particularly when dealing with linked lists. In this blog, we'll cover the problem statement, discuss a brute force approach, give hints, and present an efficient solution with its time and space complexity.

## Understanding the Problem Statement

You are given a singly linked list and need to remove the Nth node from the end of the list. The problem's goal is to modify the list in-place and return its head after removing the node. For example, given the list 1 → 2 → 3 → 4 → 5 and N = 2, the resulting list should be 1 → 2 → 3 → 5.

## Brute Force Approach

A common brute force approach to solve this problem would be:

1. First, traverse through the entire linked list to determine its length, `L`.
    
2. Calculate the position of the Nth node from the start: `L - N + 1`.
    
3. Traverse the linked list again to this calculated position.
    
4. Update pointers to remove the desired node.
    

This approach, however, requires two passes through the list, which makes it inefficient for larger linked lists.

## Hint to Solve the Problem Efficiently

A more efficient solution can be implemented by utilizing the "two-pointer technique". By using two pointers—one called `fast` and one called `slow`—you can keep a gap of `n` nodes between them and traverse the list in a single pass. This technique helps to directly reach the node that needs to be removed without the need to calculate its position.

## Efficient Solution

Let's walk through an efficient approach that uses only one pass, based on the given code:

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # Create a dummy node to simplify edge cases
        dummy.next = head
        slow, fast = dummy, head
        
        # Move fast pointer so that the gap between slow and fast is n nodes apart
        for _ in range(n):
            fast = fast.next
        
        # Move fast to the end, maintaining the gap
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Skip the desired node
        slow.next = slow.next.next

        # Return head of the modified list
        return dummy.next
```

**Explanation:**

1. A dummy node is created to handle edge cases (e.g., when the node to be removed is the head).
    
2. Two pointers—`slow` and `fast`—are initialized, with the `fast` pointer starting at the head and the `slow` pointer starting at the dummy node.
    
3. The `fast` pointer moves ahead by `n` nodes, creating a gap of `n` nodes between `slow` and `fast`.
    
4. Both pointers move one node at a time until `fast` reaches the end of the list.
    
5. The `slow` pointer is now just before the node that needs to be removed. The next pointer of `slow` is updated to skip the node to be removed.
    
6. Finally, the modified list's head is returned.
    

## Time and Space Complexity

* **Time Complexity:** The time complexity for this solution is **O(N)**, where `N` is the number of nodes in the linked list. This is because we only make one pass through the list.
    
* **Space Complexity:** The space complexity is **O(1)**, as we are only using a few pointers and not allocating any extra space for data structures that grow with the input size.
    

The two-pointer approach is efficient and ideal for solving this problem in a single traversal, making it a significant improvement over the brute force approach.

## Conclusion

The "Remove Nth Node From End of List" problem is a great example of how linked list problems can often be solved efficiently using pointer manipulation. By understanding the two-pointer technique, we can solve this problem in a single traversal, optimizing both time and space complexity. This approach not only demonstrates an efficient solution but also highlights the importance of using dummy nodes to simplify edge cases in linked list operations. Mastering these techniques will greatly enhance your ability to solve similar linked list problems in coding interviews.


README for [Remove Nth Node From End of List (Leetcode #19)](https://blog.unwiredlearning.com/remove-nth-node-from-end-of-list) was compiled from the Unwired Learning Blog.