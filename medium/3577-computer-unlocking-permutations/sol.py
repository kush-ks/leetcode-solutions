class Solution:
    def countPermutations(self, nums: List[int]) -> int:
        ans = 1
        MOD = pow(10,9)+7
        root = nums[0]

        for i in range(1,len(nums)):
            if nums[i] <= root:
                ans = 0
                break
            ans = (ans * i) % MOD


        return ans