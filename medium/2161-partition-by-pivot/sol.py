class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser, equal, higher = 0, 0, 0
        n = len(nums)

        for num in nums:
            if num < pivot:     lesser += 1
            elif num == pivot:  equal  += 1
        
        lessStart = 0
        equalStart = lesser
        higherStart = lesser + equal

        ans = [0 for _ in range(n)]    

        for num in nums:
            if num < pivot:
                ans[lessStart] = num
                lessStart += 1
            elif num == pivot:
                ans[equalStart] = num
                equalStart += 1
            else:
                ans[higherStart] = num
                higherStart += 1


        return ans