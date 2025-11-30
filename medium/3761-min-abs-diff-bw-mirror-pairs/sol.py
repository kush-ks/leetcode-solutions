from collections import defaultdict

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        def rev(x):
            rev = 0
            while x > 0:
                rev = rev*10 + x%10
                x //= 10
            return rev
            
        
        cache = defaultdict(int)
        INF = float('inf')
        ans = INF

        for i, num in enumerate(nums):
            if num in cache:
                ans = min(ans,abs(i-cache[num]))
            cache[rev(num)] = i

        return ans if ans != INF else -1 