class Solution {
public:

    int helper_function(vector<int>& nums, int goal){
        if(goal < 0){
            return 0;
        }
        int res = 0;
        int curr = 0;
        int l = 0, r = 0;

        while(r < nums.size()){
            curr += nums[r];
            while(curr > goal){
                curr -= nums[l];
                l += 1;
            }
            res += (r - l + 1);
            r += 1;
        }
        return res;
    }
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        return helper_function(nums, goal) - helper_function(nums, goal - 1);

    }
};