class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        totalSum = 0
        windSum = 0
        modifiedWind = 0

        n = len(prices)

        for i in range(n):
            totalSum += prices[i] * strategy[i]
            if i < k: windSum += prices[i] * strategy[i]
            if k//2 <= i < k: modifiedWind += prices[i]
        
        maxProfit = totalSum
        l,r = 0,k-1

        while r < n:
            maxProfit = max(maxProfit, totalSum - windSum + modifiedWind)

            windSum -= prices[l] * strategy[l]
            modifiedWind -= prices[l + k//2]
            
            l,r = l+1,r+1
            if r < n:
                windSum += prices[r] * strategy[r]
                modifiedWind += prices[r]
        
        
        return maxProfit