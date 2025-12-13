class Solution:
    def numTrees(self, n: int) -> int:
        def subTreeWays(x):
            nonlocal ways
            # return cache
            if ways[x]: 
                return ways[x]
            # compute for this nodes subtree
            ans = 0
            for i in range(x):
                left  = subTreeWays(i)
                right = subTreeWays(x-1-i)
                ans += left * right
            # save to cache and return
            ways[x] = ans
            return ans


        ways = [0 for _ in range(n+1)]
        ways[0] = ways[1] = 1

        return subTreeWays(n)
