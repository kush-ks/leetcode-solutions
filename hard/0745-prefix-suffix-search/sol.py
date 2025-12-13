class WordFilter:
    class Trie:
        def __init__(self):
            self.next = [None for _ in range(26)]
            self.end = False
            self.index = -1
            self.word = None


    def __init__(self, words: List[str]):
        self.head = self.Trie()

        for i, word in enumerate(words):
            ptr = self.head
            n = len(word)
            for j in range(n):
                asci = ord(word[j])-97
                if not ptr.next[asci]:
                    ptr.next[asci] = self.Trie() 
                ptr = ptr.next[asci]
                if j == n-1:
                    ptr.end = True
                    ptr.index = i
                    ptr.word = word[::-1]



    def f(self, pref: str, suff: str) -> int:
        ptr = self.head
        ans, k = -1, len(suff)
        suff = suff[::-1]

        for ch in pref:
            asci = ord(ch)-97
            if not ptr.next[asci]:
                return ans
            ptr = ptr.next[asci]
        
        st = []
        st.append(ptr)

        while st:
            node = st.pop()
            if node.end and node.word[:k] == suff:
                ans = max(ans, node.index)
            for x in node.next:
                if x: st.append(x)


        return ans
        
