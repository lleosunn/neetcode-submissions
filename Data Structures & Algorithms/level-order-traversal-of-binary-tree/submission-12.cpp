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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr) return vector<vector<int>>();
        vector<vector<int>> out;
        std::queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) { // should loop for each level
            int num_nodes = q.size();
            vector<int> cur_level = {};
            for (int i = 0; i < num_nodes; ++i) {
                TreeNode* cur_node = q.front();
                q.pop();
                cur_level.push_back(cur_node->val);
                if (cur_node->left != nullptr) q.push(cur_node->left);
                if (cur_node->right != nullptr) q.push(cur_node->right);
            }
            out.emplace_back(cur_level);
        }
        return out;
    }
};
