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
        int bign = 0;
        ListNode* cur = head;
        while (cur != null) {
            ++bign;
            cur = cur.next();
        }

        int remove_index = bign - n;
        if (remove_index == 0) return head.next();
        cur = head;
        for (int i = 0; i < remove_index - 1; ++i) {
            cur = cur.next();
        }
        cur.next = cur.next.next();
        return head;
    }
};
