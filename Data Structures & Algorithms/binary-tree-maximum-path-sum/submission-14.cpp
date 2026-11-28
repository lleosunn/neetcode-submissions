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
    int maxPathSum(TreeNode* root) {
        int best = root->val;
        dfs(root, best);
        return best;
    }

private:
    int dfs(TreeNode* root, int& best) {
        if (!root) return 0;

        int best_left = max(dfs(root->left, best), 0);
        int best_right = max(dfs(root->right, best), 0);

        best = max(best, root->val + best_left + best_right);

        return root->val + max(best_left, best_right);
    }


};