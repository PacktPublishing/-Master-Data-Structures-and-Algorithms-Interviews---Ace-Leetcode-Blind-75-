#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) {
            return nullptr;
        }
        if (lists.size() == 1) {
            return lists[0];
        }

        int mid = lists.size() / 2;
        vector<ListNode*> leftLists(lists.begin(), lists.begin() + mid);
        vector<ListNode*> rightLists(lists.begin() + mid, lists.end());

        ListNode* left = mergeKLists(leftLists);
        ListNode* right = mergeKLists(rightLists);

        return mergeTwoLists(left, right);
    }

private:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy;
        ListNode* node = &dummy;

        while (l1 && l2) {
            if (l1->val < l2->val) {
                node->next = l1;
                l1 = l1->next;
            } else {
                node->next = l2;
                l2 = l2->next;
            }
            node = node->next;
        }

        node->next = l1 ? l1 : l2;
        return dummy.next;
    }
};
