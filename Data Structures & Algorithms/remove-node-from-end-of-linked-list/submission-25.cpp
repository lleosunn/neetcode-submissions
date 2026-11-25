/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int bign = 1;
        ListNode* cur = head;
        while (cur->next != nullptr) {
            ++bign;
            cur = cur->next;
        }

        int remove_index = bign - n;
        if (remove_index == 0) {
            ListNode* out = head->next;
            head->next = nullptr;
            delete head;
            return out;
        }
        cur = head;
        for (int i = 0; i < remove_index - 1; ++i) {
            cur = cur->next;
        }
        ListNode* del = cur->next;
        cur->next = cur->next->next;
        delete del;
        return head;
    }
};
