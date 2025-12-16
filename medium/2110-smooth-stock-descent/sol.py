class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 1

        ans = 0
        l,r = 0,0

        # compute ranges ---------------------
        for i in range(1,n+1):
            if i != n and prices[i-1] - prices[i] == 1:
                r = i
            else:
                k = r-l+1
                ans += (k*(k+1))//2 
                l = r = i
        

        return ans