class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(); // Initialize a dummy node
        ListNode node = dummy;

        // Traverse both lists and attach the smaller node
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                node.next = list1;
                list1 = list1.next;
            } else {
                node.next = list2;
                list2 = list2.next;
            }
            node = node.next;
        }

        // Attach any remaining nodes
        if (list1 != null) {
            node.next = list1;
        } else {
            node.next = list2;
        }

        return dummy.next; // Return the merged list
    }
}
