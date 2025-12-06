import heapq

class Solution:
    def maxPoints(self, t1: List[int], t2: List[int], k: int) -> int:
        heap = []
        ans = 0
        used = set()
        
        for i in range(len(t1)):
            diff = t1[i] - t2[i]
            heapq.heappush(heap,(-diff,i))

        for _ in range(k):
            _, i = heapq.heappop(heap)
            ans += t1[i]
            used.add(i)

        for i in range(len(t1)):
            if i not in used:
                ans += max(t1[i],t2[i])

        return ans         
        