class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        INF = float('inf')
        a,b = INF, INF
        ans = False

        for num in nums:
            if num < a:
                a = num
            elif num < b and num != a:
                b = num
            elif num > b:
                ans = True
                break
        
        return ans