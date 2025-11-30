class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # fill diagonals with 1
        for i in range(n):
            dp[i][i] = 1
        
        # from bottom to top build-up
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if s[j] == s[i]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i+1][j])

        return dp[0][n-1]