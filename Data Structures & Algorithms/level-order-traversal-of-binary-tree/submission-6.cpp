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

# include <queue>

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr) return vector<vector<int>>();
        vector<vector<int>> out = {};
        int nodes_in_cur_level = 1;
        std::queue<TreeNode*> q;
        q.push(root);
        while (q.size() != 0) { // should loop for each level
            int nodes_in_next_level = 0;
            vector<int> cur_level = {};
            for (int i = 0; i < nodes_in_cur_level; ++i) {
                TreeNode* cur_node = q.front();
                q.pop();
                cur_level.push_back(cur_node->val);
                if (cur_node->left != nullptr) {
                    q.push(cur_node->left);
                    ++nodes_in_next_level;
                }
                if (cur_node->right != nullptr) {
                    q.push(cur_node->right);
                    ++nodes_in_next_level;
                }
            }
            nodes_in_cur_level = nodes_in_next_level;
            out.push_back(cur_level);
        }
        return out;
    }
};
