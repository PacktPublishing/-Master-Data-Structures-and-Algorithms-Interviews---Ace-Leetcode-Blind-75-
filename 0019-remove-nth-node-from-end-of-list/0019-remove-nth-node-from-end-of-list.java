class ListNode {
    int val;
    ListNode next;
    ListNode(int val) {
        this.val = val;
    }
}

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode slow = dummy;
        ListNode fast = head;

        // Move fast pointer so that the gap between slow and fast is n nodes apart
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }

        // Move fast to the end, maintaining the gap
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }

        // Skip the desired node
        slow.next = slow.next.next;

        return dummy.next;
    }
}