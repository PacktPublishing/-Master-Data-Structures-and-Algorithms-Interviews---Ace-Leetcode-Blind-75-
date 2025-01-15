#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy; // Initialize a dummy node
        ListNode* node = &dummy;

        // Traverse both lists and attach the smaller node
        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val < list2->val) {
                node->next = list1;
                list1 = list1->next;
            } else {
                node->next = list2;
                list2 = list2->next;
            }
            node = node->next;
        }

        // Attach any remaining nodes
        if (list1 != nullptr) {
            node->next = list1;
        } else {
            node->next = list2;
        }

        return dummy.next; // Return the merged list
    }
};
