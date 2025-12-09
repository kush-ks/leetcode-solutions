from collections import defaultdict

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        count = defaultdict(list)
        ans = 0
        z = 0
        MOD = pow(10,9) + 7

        for num in nums:
            if num == 0:
                z += 1
            else:
                # count 'j' after 'i' seen
                if num in count:
                    count[num][-1] = (count[num][-1] + 1) % MOD

                # mark 'i' and 'k'
                if not num&1:
                    count[num//2].append(0)
        

        for v in count.values():
            n = len(v)
            if n > 1:
                for i in range(n-1):
                    ans = (ans + v[i]*(n-i-1)*(i+1)) % MOD

        if z > 2:
            ans = (ans + (z*(z-1)*(z-2) // 6) % MOD) % MOD

        return ans