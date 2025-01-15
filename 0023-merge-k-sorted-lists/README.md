# Merge k Sorted Lists (Leetcode #23)

The "Merge k Sorted Lists" problem is a well-known challenge in technical interviews, often used to assess a candidate's ability to efficiently manipulate linked lists and implement advanced merging techniques. The problem asks you to merge `k` sorted linked lists into one sorted linked list. This requires careful thought to maintain efficiency, especially when dealing with a large number of lists.

In this blog, we'll explore both a brute force approach and an efficient divide and conquer solution to solve this problem, explaining each step in detail.

## Understanding the Problem Statement

The "Merge k Sorted Lists" is a common problem in coding interviews and requires a good understanding of linked lists and efficient merging techniques. The problem is defined as follows: Given an array of `k` linked lists, each of which is sorted in ascending order, merge all these linked lists into one sorted linked list and return it.

Imagine you are provided with multiple linked lists, each of which is already sorted, and your task is to combine them into a single sorted linked list. The challenge is to do this as efficiently as possible.

**Example:**

* **Input:** `lists = [1 -> 4 -> 5, 1 -> 3 -> 4, 2 -> 6]`
    
* **Output:** `1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6`
    

The output must be a single linked list that merges all the input linked lists in a sorted manner.

## Brute Force Approach

The brute force solution involves collecting all nodes from the linked lists, storing their values in an array, sorting the array, and then reconstructing a linked list from the sorted values.

**Steps:**

1. Traverse all the linked lists and store the values of each node in an array.
    
2. Sort the array.
    
3. Create a new linked list using the sorted values.
    

**Time Complexity:**

* This approach has a time complexity of `O(N log N)`, where `N` is the total number of nodes in all the linked lists.
    
* Sorting the array takes `O(N log N)`, and the time to recreate the linked list is `O(N)`.
    

**Space Complexity:**

* Storing all the node values requires `O(N)` extra space.
    

Although straightforward, this approach is inefficient for large values of `k` and `N` since it does not take advantage of the sorted nature of the linked lists.

## Hint to Solve the Problem Efficiently

To solve the problem efficiently, think about how you can dynamically keep track of the smallest value among all the heads of the linked lists. A good way to accomplish this is by using a **divide and conquer** strategy. By merging the lists in pairs recursively, you can efficiently manage the merging process and keep the time complexity lower compared to a brute force approach.

## Efficient Solution

The provided code utilizes a **divide and conquer** technique to solve the problem. Here's how it works:

1. If there are no lists, return `None`.
    
2. If there is only one list, return it.
    
3. Split the list of linked lists into two halves and recursively merge each half.
    
4. Merge the two halves using a helper function `mergeTwoLists()`.
    

**Code Explanation:**

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        # Divide the list of linked lists into two halves and merge each half recursively
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        # Merge the two halves
        return self.mergeTwoLists(left, right)
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        node = dummy

        # Merge both lists while there are still nodes in l1 and l2
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        # If one list is exhausted, append the other list
        node.next = l1 or l2
        
        return dummy.next
```

**Explanation:**

* The `mergeKLists()` function divides the list of linked lists into two halves until a base case of one list is reached.
    
* It then uses the helper function `mergeTwoLists()` to merge the two halves.
    
* The `mergeTwoLists()` function merges two sorted linked lists into one sorted linked list using a dummy node to simplify pointer operations.
    

## Time and Space Complexity

* **Time Complexity:**
    
    * The time complexity of this approach is `O(N log k)`, where `N` is the total number of nodes, and `k` is the number of linked lists.
        
    * This is because we divide the `k` lists into two halves recursively (`log k` divisions), and each merge operation takes `O(N)` time.
        
* **Space Complexity:**
    
    * The space complexity is `O(1)` for the merging operation since we are modifying pointers in the linked lists directly.
        
    * However, the recursive approach uses additional space in the function call stack, resulting in `O(log k)` space complexity for the recursion.
        

## Conclusion

The divide and conquer approach provides a more efficient way to solve the "Merge k Sorted Lists" problem compared to the brute force approach. By splitting the list of linked lists and merging them recursively, the time complexity is reduced significantly, making this approach more suitable for larger inputs.


README for [Merge k Sorted Lists (Leetcode #23)](https://blog.unwiredlearning.com/merge-k-sorted-lists) was compiled from the Unwired Learning Blog.