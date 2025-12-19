class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lenS, lenP = len(s), len(p)
        ofs = lenS

        # edge cases
        if lenP == lenS == 0:   return True
        if lenP == 0:           return False
        if lenS == 0:           return p.count('*') == lenP

        dp = [[False for _ in range(lenS)] for _ in range(2)]
        r = 0

        for i in range(lenP-1,-1,-1):
            pattern = p[i]
            matched = False if pattern != '?' and pattern != '*' else True
            for j in range(lenS-1,-1,-1):
                ch = s[j]
                prev = dp[r^1][j+1] if j < lenS-1 else True

                # handle offset
                if j >= ofs:
                    dp[r][j] = dp[r^1][j] if pattern == '*' else False

                # handle remaining
                elif j < ofs:
                    if pattern == '*':   dp[r][j] = dp[r^1][j] | (dp[r][j+1] if j < lenS-1 else True)
                    elif pattern == '?': dp[r][j] = prev
                    else:                
                        dp[r][j] = prev if ch == pattern else False 
                        matched |= dp[r][j]

            if not matched:
                dp[r^1][0] = False
                break

            # increase offset
            if pattern != '*': ofs -= 1

            # switch rows
            r ^= 1
        

        return dp[r^1][0]