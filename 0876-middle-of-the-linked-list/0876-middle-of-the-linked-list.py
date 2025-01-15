# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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
    
    
#Question: https://leetcode.com/problems/middle-of-the-linked-list
#Blog: https://blog.unwiredlearning.com/middle-of-the-linked-list