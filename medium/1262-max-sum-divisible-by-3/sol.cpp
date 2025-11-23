class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        int sum = 0;
        int k = 0;
        int smallestOne = 10003, smallestTwo = 10004;
        
        for(int i=0;i<nums.size();i+=1) {
            sum += nums[i];
            k = nums[i]%3;
            if(k) {
                if(k==1) {
                    if((nums[i]+smallestOne) < smallestTwo)
                        smallestTwo = nums[i]+smallestOne;    
                    if(nums[i] < smallestOne) 
                        smallestOne = nums[i];                 
                }
                    
                else if(k==2) {
                    if((nums[i]+smallestTwo) < smallestOne)
                        smallestOne = nums[i]+smallestTwo;
                    if(nums[i] < smallestTwo) 
                        smallestTwo = nums[i];
                }
            }
        }
        
        k = sum % 3;
        if(k==1)        sum -= smallestOne;
        else if(k==2)   sum -= smallestTwo;

        return sum;
    }
};
