class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, pow(10,6)
        s = 0
        ans = 1

        while low <= high:
            mid = low + (high-low)//2
            s = 0
            flag = False

            for num in nums:
                s += (num+mid-1) // mid
                if s > threshold:
                    low = mid+1
                    flag = True
                    break
            
            if flag: continue
            ans = mid
            high = mid-1
        

        return ans