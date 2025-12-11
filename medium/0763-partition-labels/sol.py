from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = [-1 for _ in range(26)]
        n = len(s)
        maxSize = defaultdict(int)
        ans = []

        for i in range(n):
            ch = s[i]
            asci = ord(ch)-97
            if index[asci] == -1:
                index[asci] = i
                maxSize[i] = i
            else:
                for j in range(26):
                    if index[j] != index[asci] and index[asci] < index[j] < i:
                        index[j] = index[asci]
                maxSize[index[asci]] = i


        for ch in s:
            asci = ord(ch)-97
            i = index[asci]
            if maxSize[i] == -1: continue
            ans.append(maxSize[i] - i + 1)
            maxSize[i] = -1


        return ans