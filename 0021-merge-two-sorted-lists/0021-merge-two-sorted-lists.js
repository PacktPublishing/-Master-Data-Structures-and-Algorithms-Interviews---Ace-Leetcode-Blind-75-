class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

function mergeTwoLists(list1, list2) {
    let dummy = new ListNode(); // Initialize a dummy node
    let node = dummy;

    // Traverse both lists and attach the smaller node
    while (list1 !== null && list2 !== null) {
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
    node.next = list1 !== null ? list1 : list2;

    return dummy.next; // Return the merged list
}
