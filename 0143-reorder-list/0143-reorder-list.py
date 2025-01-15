# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        previous, current = None, slow
        while current:
            next_temp = current.next
            current.next = previous
            previous = current
            current = next_temp

        # Step 3: Merge the two halves
        first, second = head, previous
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        
        
#Question: https://leetcode.com/problems/reorder-list
#Blog: https://blog.unwiredlearning.com/reorder-list