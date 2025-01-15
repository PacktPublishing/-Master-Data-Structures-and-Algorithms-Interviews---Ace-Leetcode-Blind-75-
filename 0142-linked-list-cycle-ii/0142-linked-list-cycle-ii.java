public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        // Advance both pointers at different speeds until they meet
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;

            // If they meet, start from the head again and move at the same speed
            if (slow == fast) {
                while (head != slow) {
                    head = head.next;
                    slow = slow.next;
                }
                return slow;
            }
        }

        // If no cycle is detected, return null
        return null;
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}