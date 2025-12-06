class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # 3 - 1 = 2 and 4 -2 = 2 -> O,O or E,E (0 = E)
        n = len(nums)
        pre = [0 for _ in range(n)]
        ans = 0

        for i, num in enumerate(nums):
            pre[i] = nums[i] + (pre[i-1] if i>0 else 0)
        
        for i in range(n-1):
            a,b = pre[i], pre[n-1] - pre[i]
            if not (a&1)^(b&1):
                ans += 1
        
        return ans