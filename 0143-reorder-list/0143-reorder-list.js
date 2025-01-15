class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

function reorderList(head) {
    if (head === null) return;
    
    // Step 1: Find the middle of the linked list
    let slow = head, fast = head;
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    // Step 2: Reverse the second half of the list
    let previous = null, current = slow;
    while (current !== null) {
        let nextTemp = current.next;
        current.next = previous;
        previous = current;
        current = nextTemp;
    }
    
    // Step 3: Merge the two halves
    let first = head, second = previous;
    while (second.next !== null) {
        let temp1 = first.next;
        let temp2 = second.next;
        first.next = second;
        second.next = temp1;
        first = temp1;
        second = temp2;
    }
}