from collections import defaultdict
from linecache import cache

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        @cache
        def fact(x):
            if x == 0 or x == 1:   return 1
            p = 1
            for i in range(2,x+1):
                p *= i
            return p
        
        @cache
        def combination(n,r):
            return fact(n) // (fact(r) * fact(n-r))
        
        ans, s = 0, 0
        MOD = pow(10,9)+7
        lines = defaultdict(list)
        multiPoints = set()

        for x,y in points:
            if y in lines:  lines[y][0] += 1
            else:           lines[y] = [1,0]
            if lines[y][0] == 2:
                multiPoints.add(y)
        
        for y in multiPoints:
            lines[y][1] = combination(lines[y][0],2)
            s += lines[y][1]
        
        for y in multiPoints:
            ans = (ans + ((s-lines[y][1]) * lines[y][1]) % MOD) % MOD
            s -= lines[y][1]

        return ans
            