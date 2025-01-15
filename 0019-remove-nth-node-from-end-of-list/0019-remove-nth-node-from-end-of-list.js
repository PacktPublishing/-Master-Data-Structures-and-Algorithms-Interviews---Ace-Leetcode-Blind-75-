class ListNode {
    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}

function removeNthFromEnd(head, n) {
    let dummy = new ListNode(0);
    dummy.next = head;
    let slow = dummy;
    let fast = head;

    // Move fast pointer so that the gap between slow and fast is n nodes apart
    for (let i = 0; i < n; i++) {
        fast = fast.next;
    }

    // Move fast to the end, maintaining the gap
    while (fast !== null) {
        fast = fast.next;
        slow = slow.next;
    }

    // Skip the desired node
    slow.next = slow.next.next;

    return dummy.next;
}