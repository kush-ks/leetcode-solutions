class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        globalSum = float('-inf')
        currSum = 0
        sums = [0 for _ in range(k)]

        for i in range(k):
            currSum += nums[i]
        
        globalSum = max(globalSum,currSum)
        sums[0] = max(0,currSum)
        
        for i in range(k,len(nums)):
            x = (i-k+1)%k
            currSum += nums[i] - nums[i-k]
            globalSum = max(globalSum,currSum+sums[x])
            sums[x] = max(0,currSum+sums[x])

        return globalSum