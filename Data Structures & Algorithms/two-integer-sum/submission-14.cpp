class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> num_to_index;
        int size = static_cast<int>(nums.size());

        for (int i = 0; i < size; ++i) {
            if (num_to_index.contains(target - nums[i])) {
                return {num_to_index[target - nums[i]], i};
            } else num_to_index[nums[i]] = i;
        }
    }
};
