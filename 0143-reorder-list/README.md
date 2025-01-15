# Reorder List (Leetcode #143)

LeetCode's problem 143, **"Reorder List,"** is a challenging yet rewarding question. Here, I'll walk you through the problem, a common brute force solution, and then guide you to the efficient solution using the attached code, helping you understand how to reorder a linked list step by step.

## Understanding the Problem Statement

The task requires us to reorder a given singly linked list, defined as:

* Given the head of a singly linked list, modify it in such a way that the nodes are reordered from their original sequence in the pattern: first node, last node, second node, second last node, and so on.
    
* Specifically, given a list like `1 -> 2 -> 3 -> 4 -> 5`, the reordered list should be `1 -> 5 -> 2 -> 4 -> 3`.
    

The aim is to do this **in-place** without altering the node values or using extra memory in the form of a new list.

## Brute Force Approach

The brute force approach to solve this problem involves copying all the elements of the linked list to an array or a list, rearranging the values in the desired order, and then repopulating the original linked list. Though straightforward, this approach violates the in-place requirement of the problem and requires **O(n)** additional space.

* **Steps:** Traverse the linked list and store its nodes in an array. Then, using two pointers, reorder them into the specified pattern and rebuild the linked list accordingly.
    
* **Time Complexity:** This approach takes **O(n)** for the traversal and reordering but also uses **O(n)** space, which is not ideal.
    

## Hint to Solve the Problem Efficiently

Instead of storing nodes in a list, think of breaking down the list in two parts, reversing one half, and then merging them back. Imagine the process as finding the **middle point** of the list and strategically reordering.

## Efficient Solution

The attached code uses a three-step approach to solve the problem efficiently while ensuring we keep the space complexity at **O(1)**. Here is a breakdown:

1. **Find the Middle of the Linked List**
    
    We use two pointers, `slow` and `fast`, to find the middle node of the list. The `fast` pointer moves twice as fast as the `slow` pointer, meaning by the time `fast` reaches the end of the list, `slow` will be at the middle. This gives us the split point to divide the list into two halves.
    
    ```python
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    ```
    
2. **Reverse the Second Half of the List**
    
    The next step involves reversing the second half of the list, starting from the node `slow`. We use three pointers: `previous`, `current`, and `next_temp` to reverse the nodes iteratively until we reach the end of the list.
    
    ```python
    previous, current = None, slow
    while current:
        next_temp = current.next
        current.next = previous
        previous = current
        current = next_temp
    ```
    
    At the end of this step, `previous` will point to the new head of the reversed second half.
    
3. **Merge the Two Halves**
    
    Finally, we merge the two halves together. We use two pointers, `first` and `second`, representing the first and second halves respectively. We alternate linking nodes from each half, ensuring the new reordered structure is achieved.
    
    ```python
    first, second = head, previous
    while second.next:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2
    ```
    

## Time and Space Complexity

* **Time Complexity:** The solution takes **O(n)** time since each of the three main steps (finding the middle, reversing the second half, and merging) involves a linear traversal of the linked list.
    
* **Space Complexity:** The solution operates with **O(1)** additional space, making it an in-place solution that satisfies the problem's constraints.
    

## Conclusion

The problem requires us to reorder a singly linked list in a particular pattern, and while a brute force approach may seem feasible, the efficient method involves using pointer manipulation to achieve an in-place solution. By dividing, reversing, and merging the list, we achieve the desired outcome effectively with a linear time complexity and constant space complexity.


README for [Reorder List (Leetcode #143)](https://blog.unwiredlearning.com/reorder-list) was compiled from the Unwired Learning Blog.