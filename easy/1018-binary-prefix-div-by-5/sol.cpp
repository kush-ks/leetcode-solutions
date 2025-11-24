#include <vector>

class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        vector<bool> ans(nums.size(), false);
        int num = 0;

        for(int i=0;i<nums.size();i+=1) {
            num <<= 1;
            num = (num + nums[i]) % 10;
            ans[i] = num==0 || num==5;
        }

        return ans;
    }
};