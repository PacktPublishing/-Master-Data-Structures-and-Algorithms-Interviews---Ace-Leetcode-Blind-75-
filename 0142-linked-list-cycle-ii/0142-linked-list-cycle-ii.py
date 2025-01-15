# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
    

#Question: https://leetcode.com/problems/linked-list-cycle-ii
#Blog: https://blog.unwiredlearning.com/linked-list-cycle-ii