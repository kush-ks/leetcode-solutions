from linecache import cache

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        @cache
        def asci(ch):   return ord(ch)-97

        INF = float('inf')
        ranges = [[INF,INF] for _ in range(26)]
        dp = [[0 for _ in range(26)] for _ in range(26)]
        ans = 0

        for i in range(len(s)):
            j = asci(s[i])
            if ranges[j][0] == INF: ranges[j][0] = i
            else:                   ranges[j][1] = i
        
        for i in range(len(s)):
            c = asci(s[i])
            for j in range(26):
                if ranges[j][0] == INF: continue
                if ranges[j][1] != INF and dp[j][c] == 0 and ranges[j][0] < i < ranges[j][1]:
                    dp[j][c] = 1
                    ans += 1

        return ans 