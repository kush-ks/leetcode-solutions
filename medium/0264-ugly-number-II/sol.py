import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        heapq.heappush(heap,1)
        seen = set()

        for _ in range(n-1):
            x = heapq.heappop(heap)
            if x*2 not in seen:
                heapq.heappush(heap,x*2)
                seen.add(x*2)
            if x*3 not in seen:
                heapq.heappush(heap,x*3)
                seen.add(x*3)
            if x*5 not in seen:
                heapq.heappush(heap,x*5)
                seen.add(x*5)
        
        return heapq.heappop(heap)