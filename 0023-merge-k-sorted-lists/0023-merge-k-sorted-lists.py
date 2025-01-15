# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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
    

#Question: https://leetcode.com/problems/merge-k-sorted-lists
#Blog: https://blog.unwiredlearning.com/merge-k-sorted-lists