class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size()
        std::unordered_map<int, int> prev; // Maps prev numbers to their index
        for (int i = 0; i < n; i++) {
            int diff = nums[i] - target;
            if (prev.count(diff) == 1) {
                return {prev[diff], i};
            }
            prev.insert({nums[i], i});
        }
        return {};
    }
};
