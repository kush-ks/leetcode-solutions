class Solution:
    def maxDistinct(self, s: str) -> int:
        used = [False for _ in range(26)]
        ans = 0

        for ch in s:
            asci = ord(ch) - 97
            if not used[asci]:
                ans += 1
                used[asci] = True
                
        return ans