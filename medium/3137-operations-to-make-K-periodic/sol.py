class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        curr = 0
        n = len(word)
        total = n // k
        f = {}

        for i in range(0,n,k):
            w = word[i:i+k]
            if w in f: f[w] += 1
            else: f[w] = 1
            curr = max(curr,f[w])
        
        return total - curr