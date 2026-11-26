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

 /*
for (ListNode* node : lists) {} // Iterate vector
lists.size(); lists.empty();

priority_queue<ListNode*, vector<ListNode*>, Compare> pq;
pq.push(node);
ListNode* node = pq.top();
pq.pop();
pq.size();
pq.empty();

ListNode dummy(0);
ListNode* cur = &dummy;
cur->next = node;
cur = cur->next;

if (node) {}  // Not null
if (!node) {} // Null
while (!pq.empty()) {}

return dummy.next;
*/

/*
solution i was thinking of:
build minheap, each entry of the minheap is a linked list,
sorted by the value at the head of the list
while the heap is not empty:
pop the top of the heap and assemble the final linked list that way
priority_queue in cpp is how u would implement this

we need something to compare priority_queue entries
*/
struct Compare {
    bool operator()(ListNode* a, ListNode* b) {
        return a->val > b->val; // min heap
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // create min heap
        std::priority_queue<ListNode*, vector<ListNode*>, Compare> pq(lists.begin(), lists.end());
        for (ListNode* node : lists) {
            if (node != null) pq.push(node);
        }

        ListNode dummy(0);
        ListNode* cur = &dummy; // advance as i build the list
        while (pq.size() > 0) {
            ListNode* top = pq.top();
            pq.pop();
            cur->next = top;
            cur = cur->next;
            if (top->next != nullptr) pq.push(top->next);
        }
        return dummy.next;
    }
};





