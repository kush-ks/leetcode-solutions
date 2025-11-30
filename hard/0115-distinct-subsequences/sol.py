from collections import defaultdict

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(t),len(s)
        if m > n: return 0
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        seen = defaultdict(int)

        for j in range(n+1):
            dp[0][j] = 1

        for i in range(1,m+1):
            asci = ord(t[i-1])-97
            freq = seen[asci]

            for j in range(1,n+1):
                dp[i][j] = dp[i][j-1]
                if t[i-1] == s[j-1]:
                    if freq > 0: 
                        freq -= 1
                        continue
                    dp[i][j] += dp[i-1][j-1]

            seen[asci] += 1


        return dp[m][n]