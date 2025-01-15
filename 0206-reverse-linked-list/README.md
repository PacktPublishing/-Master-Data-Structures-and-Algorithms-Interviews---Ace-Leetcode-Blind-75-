# Reverse Linked List (Leetcode #206)

Linked Lists are fundamental data structures, and many problems revolve around manipulating them in some way. The problem '206. Reverse Linked List' asks us to reverse a singly linked list, a basic yet crucial exercise to build your problem-solving skills in linked lists. Let’s break down the problem, explore a common brute force approach, and discuss the efficient solution, along with the time and space complexity.

## Understanding the Problem Statement

In this problem, you are given the head of a singly linked list, and you need to reverse it. Essentially, this means that the last node should become the first node, the second-last node should become the second node, and so on until the original first node is the last one.

The main objective is to return the head of this newly reversed linked list.

Example:

* **Input**: 1 -&gt; 2 -&gt; 3 -&gt; 4 -&gt; 5 -&gt; None
    
* **Output**: 5 -&gt; 4 -&gt; 3 -&gt; 2 -&gt; 1 -&gt; None
    

## Brute Force Approach

The brute force approach involves using an auxiliary data structure to store the nodes of the linked list. Here’s how it typically works:

1. Traverse the linked list and store all the node values in an array or list.
    
2. Then iterate over this array in reverse order to recreate the linked list, pointing each node to its preceding one.
    

While this approach is easy to implement and might seem straightforward, it has high space complexity since we use an additional list to store the node values.

* **Time Complexity**: O(N) - We need to traverse all nodes twice, once to collect data and once to recreate the list.
    
* **Space Complexity**: O(N) - Extra space is used to store node values in an array.
    

## Hint to Solve the Problem Efficiently

To solve this problem efficiently without using extra space, think about manipulating the pointers of the nodes in-place rather than copying the data into another data structure. We can reverse the linked list by reassigning each node’s `next` pointer to its previous node, proceeding one node at a time.

## Efficient Solution

Let’s walk through the provided solution which is implemented in Python:

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, previous and current.
        # Previous will eventually become the new head of the reversed list.
        previous, current = None, head

        # Traverse the list until we reach the end.
        while current:
            # Temporarily store the next node.
            temp = current.next
            
            # Reverse the 'next' pointer of the current node to point to previous node.
            current.next = previous
            
            # Move the previous pointer up to the current node.
            previous = current
            
            # Proceed to the next node in the original list.
            current = temp
        
        # After the loop, current will be None and previous will be the new head of the reversed list.
        head = previous
        return head
```

The idea here is simple but very effective. We use two pointers, `previous` and `current`, to reverse the `next` pointers of each node in the linked list as we traverse through it.

* **previous** initially points to `None` since the new tail (original head) will point to `None`.
    
* **current** starts from the head of the original list.
    
* As we iterate through the list, the next node is stored temporarily in a variable (`temp`) to prevent losing the reference.
    
* The `next` pointer of the current node is then reversed to point to the previous node.
    
* Both pointers (`previous` and `current`) are moved one step forward until the end of the list.
    

The process stops when we reach the end (`current` is `None`). At this point, `previous` points to the new head of the reversed list.

## Time and Space Complexity

* **Time Complexity**: O(N) - Where N is the number of nodes in the linked list. Each node is visited once, resulting in a linear time complexity.
    
* **Space Complexity**: O(1) - The solution is done in-place, using constant space. No extra data structures are needed other than pointers to keep track of nodes, making this solution efficient in terms of space usage.
    

The efficient approach to solving this problem not only improves your understanding of linked lists but also emphasizes the importance of optimizing pointer manipulations. By focusing on reassigning node pointers in-place, we achieve optimal time and space complexity, a crucial skill for tackling linked list challenges.

## Conclusion

Reversing a linked list is a foundational problem that helps you develop a solid understanding of linked list manipulations. The brute force approach offers a simple solution but at the cost of increased space complexity. On the other hand, the efficient in-place solution not only reduces space usage but also strengthens your ability to manage pointers effectively. Mastering this problem will make it easier to tackle more advanced linked list challenges and deepen your understanding of fundamental data structures.


README for [Reverse Linked List (Leetcode #206)](https://blog.unwiredlearning.com/reverse-linked-list) was compiled from the Unwired Learning Blog.