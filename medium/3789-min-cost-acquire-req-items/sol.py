class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans = 0
        
        if cost1 + cost2 <= costBoth:
            ans = need1*cost1 + need2*cost2
        
        else:
            req = min(need1,need2)
            excess1 = (need1-req)*min(cost1,costBoth)
            excess2 = (need2-req)*min(cost2,costBoth)
            ans = req*costBoth + excess1 + excess2

        return ans