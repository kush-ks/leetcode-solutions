class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0 for _ in range(n)]
        ans = -float('inf')
        
        currMin = nums[n-1]
        pre[0] = nums[0]

        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]

        for i in range(n-2,-1,-1):
            ans = max(ans, pre[i] - currMin)
            currMin = min(currMin, nums[i])
        
        return ans