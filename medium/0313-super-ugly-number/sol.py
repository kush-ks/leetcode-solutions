import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = []
        heapq.heappush(heap,1)
        seen = set()

        for _ in range(n-1):
            num = heapq.heappop(heap)
            for p in primes:
                if p*num not in seen:
                    heapq.heappush(heap,p*num)
                    seen.add(p*num)
        
        return heapq.heappop(heap)