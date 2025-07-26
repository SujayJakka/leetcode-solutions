class Solution {
public:
    int minimizeArrayValue(vector<int>& nums) {
        int res = nums[0];
        double total = nums[0];

        for(int i = 1; i < nums.size(); i++){
            total += nums[i];
            res = max(res, int(ceil(total / double(i + 1))));
        }

        return res;
    }
};