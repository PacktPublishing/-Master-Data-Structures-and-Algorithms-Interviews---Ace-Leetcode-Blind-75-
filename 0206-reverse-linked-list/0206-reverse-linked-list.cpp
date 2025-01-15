#include <iostream>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* previous = nullptr;
        ListNode* current = head;

        while (current != nullptr) {
            ListNode* temp = current->next;
            current->next = previous;
            previous = current;
            current = temp;
        }

        return previous;
    }
};