class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        anchor, curr = -1, 0
        i = 0
        n = len(gas)
        loop = False

        while i != anchor:
            # update available gas
            curr += gas[i] - cost[i]

            # check we can reach this point with available gas
            if curr < 0:
                curr, anchor = 0, -1
                if loop: break
            elif anchor == -1:
                anchor = i
            
            # end of list reached but no start point found
            if i == n-1 and anchor == -1:
                break   

            # re-loop to find clockwise feasible path
            if i == n-1:
                loop = True
                i = 0
            else:
                i += 1
        

        return anchor