#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head) return;
        
        // Step 1: Find the middle of the linked list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // Step 2: Reverse the second half of the list
        ListNode* previous = nullptr;
        ListNode* current = slow;
        while (current != nullptr) {
            ListNode* nextTemp = current->next;
            current->next = previous;
            previous = current;
            current = nextTemp;
        }
        
        // Step 3: Merge the two halves
        ListNode* first = head;
        ListNode* second = previous;
        while (second->next != nullptr) {
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;
            first->next = second;
            second->next = temp1;
            first = temp1;
            second = temp2;
        }
    }
};