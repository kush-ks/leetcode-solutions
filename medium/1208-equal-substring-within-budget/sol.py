class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        pre = [0 for _ in range(n)]
        curr = 0

        # build prefix sum
        for i in range(n):
            num = abs(ord(s[i]) - ord(t[i]))
            curr += num
            pre[i] = curr
        
        # 2 pointers find longest subarr with sum <= maxCost
        l,r = -1,0
        maxLen = 0  

        while r < n:
            s = pre[r] - (pre[l] if l>=0 else 0)
            if s <= maxCost:
                maxLen = max(maxLen,r-l)
                r += 1
            else:
                l += 1


        return maxLen