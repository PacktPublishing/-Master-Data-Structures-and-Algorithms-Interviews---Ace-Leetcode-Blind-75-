class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    mergeKLists(lists) {
        if (!lists || lists.length === 0) {
            return null;
        }
        if (lists.length === 1) {
            return lists[0];
        }

        const mid = Math.floor(lists.length / 2);
        const left = this.mergeKLists(lists.slice(0, mid));
        const right = this.mergeKLists(lists.slice(mid));

        return this.mergeTwoLists(left, right);
    }

    mergeTwoLists(l1, l2) {
        const dummy = new ListNode();
        let node = dummy;

        while (l1 && l2) {
            if (l1.val < l2.val) {
                node.next = l1;
                l1 = l1.next;
            } else {
                node.next = l2;
                l2 = l2.next;
            }
            node = node.next;
        }

        node.next = l1 || l2;
        return dummy.next;
    }
}
