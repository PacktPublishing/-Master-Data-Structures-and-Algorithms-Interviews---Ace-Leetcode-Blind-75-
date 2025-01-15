class ListNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

var detectCycle = function(head) {
    let slow = head;
    let fast = head;

    // Advance both pointers at different speeds until they meet
    while (fast !== null && fast.next !== null) {
        fast = fast.next.next;
        slow = slow.next;

        // If they meet, start from the head again and move at the same speed
        if (slow === fast) {
            while (head !== slow) {
                head = head.next;
                slow = slow.next;
            }
            return slow;
        }
    }

    // If no cycle is detected, return null
    return null;
};