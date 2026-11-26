/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

/*
maintain a size-k priority queue (maxheap)
dfs through the tree and update the pq
return top value of pq
*/

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        std::priority_queue<int> pq; // keep track of smallest values (maxheap)
        std::queue<TreeNode*> q; // queue for tree traversal
        q.push(root);

        while(!q.empty()) {
            TreeNode* cur = q.front();
            q.pop();
            if (!cur) continue;

            if (pq.size() < k) pq.push(cur->val);
            else {
                if (cur->val < pq.top()) {
                    pq.pop();
                    pq.push(cur->val);
                }
            }

            q.push(cur->left);
            q.push(cur->right);
        }

        return pq.top();


    }
};
