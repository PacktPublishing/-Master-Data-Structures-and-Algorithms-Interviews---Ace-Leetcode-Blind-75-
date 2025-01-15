class ListNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

function reverseList(head) {
    let previous = null;
    let current = head;

    while (current !== null) {
        let temp = current.next;
        current.next = previous;
        previous = current;
        current = temp;
    }

    return previous;
}