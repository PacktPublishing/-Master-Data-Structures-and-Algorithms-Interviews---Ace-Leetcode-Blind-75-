# Merge Two Sorted Lists (Leetcode #21)

The "Merge Two Sorted Lists" problem is a classic LeetCode problem often asked in technical interviews. It tests your understanding of linked lists and your ability to effectively merge two data structures.

## Understanding the Problem Statement

Given two sorted linked lists `list1` and `list2`, merge them into one sorted linked list. The merged list should be formed by splicing together the nodes of the original two lists. The solution should return the merged linked list.

For example:

* Input: `list1 = [1, 2, 4]`, `list2 = [1, 3, 4]`
    
* Output: `[1, 1, 2, 3, 4, 4]`
    

The key challenge is to maintain the sorted order while combining both linked lists.

## Brute Force Approach

One simple approach would be to traverse both linked lists, add all the elements to an array, and then sort the array. Afterward, we could create a new linked list using the sorted values. Here’s how this brute-force approach works:

1. Traverse through both `list1` and `list2`, adding each node’s value to an array.
    
2. Sort the array in ascending order.
    
3. Create a new linked list using the sorted values.
    

While this approach works, it does not utilize the fact that both lists are already sorted, resulting in a higher time complexity. Sorting the entire combined list costs `O((m+n) log(m+n))` where `m` and `n` are the lengths of `list1` and `list2`, respectively. Also, this solution consumes extra space for the array.

## Hint to Solve the Problem Efficiently

Since both lists are already sorted, we can merge them in a way similar to the "merge" step in the Merge Sort algorithm. Use two pointers to traverse both lists, compare the nodes, and form a new linked list without using additional space for storage.  

## Efficient Solution

Let's walk through an efficient solution that directly merges the two linked lists using the provided code:

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Initialize a dummy node
        node = dummy

        # Traverse both lists and attach the smaller node
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        # Attach any remaining nodes
        if list1 is not None:
            node.next = list1
        else:
            node.next = list2

        return dummy.next  # Return the merged list
```

The solution utilizes a dummy node to simplify the merging process. Here's how it works:

* **Initialize a Dummy Node:**  
    A dummy node is initialized to act as the start of the merged list. This makes it easier to return the merged list at the end since `dummy.next` points to the beginning of our result.
    
* **Two Pointers Traversing the Lists:**  
    We use two pointers, starting at the head of `list1` and `list2`. We compare the values at each pointer and attach the smaller value to our current node (`node`). This helps maintain the sorted order while merging.
    
* **Attach Remaining Nodes:**  
    After the while loop, one of the linked lists may still have nodes left. We attach these remaining nodes to our merged list directly.
    

The use of a dummy node helps avoid edge cases where managing the head of the merged list can become cumbersome.

## Time and Space Complexity

* **Time Complexity:**  
    The time complexity of this solution is `O(m + n)`, where `m` and `n` are the lengths of `list1` and `list2`, respectively. This is because each node is visited exactly once.
    
* **Space Complexity:**  
    The space complexity is `O(1)` since we are not using any extra data structures except the linked list nodes themselves. The solution builds the merged list in place, keeping the space utilization efficient.
    

## **Conclusion**

The "Merge Two Sorted Lists" problem is a great exercise for practicing linked list manipulation and understanding how to efficiently merge sorted data structures. The efficient solution provided here uses a dummy node to simplify the process and maintains an optimal time complexity of `O(m + n)`, making it a very effective approach for merging two sorted linked lists. Practicing this type of problem helps improve your skills in solving similar problems where merging and sorting come into play, providing an excellent foundation for more advanced data structure questions.


README for [Merge Two Sorted Lists](https://blog.unwiredlearning.com/merge-two-sorted-lists) was compiled from the Unwired Learning Blog.