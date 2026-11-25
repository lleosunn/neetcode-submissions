class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans = nums;
        return ans.insert(ans.end, ans.begin(), ans.end());
    }
};