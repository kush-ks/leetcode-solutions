import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        ans = []
        freqs = defaultdict(int)
        for w in words:
            freqs[w] += 1
        
        for w,f in freqs.items():
            heapq.heappush(heap,(-f,w))
        
        for _ in range(k):
            _, w = heapq.heappop(heap)
            ans.append(w)
        
        return ans