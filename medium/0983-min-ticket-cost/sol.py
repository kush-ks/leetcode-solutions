class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        lastDay = days[n-1]
        j = n-1
        dp = [0 for _ in range(lastDay+1)]

        for i in range(lastDay,0,-1):
            # not a trip day
            if j < 0 or i != days[j]:
                dp[i] = dp[i+1]
            
            # is a trip day
            else:
                j -= 1
                dp[i] = min(costs[0] + (dp[i+1]  if i+1  <= lastDay else 0),
                            costs[1] + (dp[i+7]  if i+7  <= lastDay else 0),
                            costs[2] + (dp[i+30] if i+30 <= lastDay else 0)
                        )


        return dp[1]