# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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
    
    
#Question: https://leetcode.com/problems/merge-two-sorted-lists
#Blog: https://blog.unwiredlearning.com/merge-two-sorted-lists