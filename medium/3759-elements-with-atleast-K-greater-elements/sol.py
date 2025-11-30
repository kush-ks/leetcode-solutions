class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans, dup = 0, 0

        for i, num in enumerate(nums):
            if i < n-1 and num == nums[i+1]:
                dup += 1
                continue
            if n-i-1 >= k:
                ans += dup+1
                dup = 0

        return ans