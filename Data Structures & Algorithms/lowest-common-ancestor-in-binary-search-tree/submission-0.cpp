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

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* smaller = nullptr;
        TreeNode* bigger = nullptr;
        if (p->val < q->val) {
            smaller = p;
            bigger = q;
        } else {
            smaller = q;
            bigger = p;
        }

        TreeNode* cur = root;
        // return cur if smaller val < cur val < bigger val or cur = p or cur = q
        while (cur != nullptr) {
            if (cur->val < smaller->val) { // move right
                cur = cur->right;
            } else if (bigger->val < cur->val) { // move left
                cur = cur->left;
            } else return cur;
        }
    }
};
