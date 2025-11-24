#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int,int> cache;
        int count = 0, maxLen = 0;
        cache[0] = -1;

        for(int i=0; i<nums.size(); i+=1) {
            count += nums[i] ? 1 : -1;
            if(cache.find(count)!=cache.end())
                maxLen = max(maxLen, i-cache[count]);
            else
                cache[count] = i;
        }   

        return maxLen;
    }
};