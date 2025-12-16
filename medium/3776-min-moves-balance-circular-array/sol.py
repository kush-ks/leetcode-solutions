class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        negAt = -1
        for i, num in enumerate(balance):
            if num < 0:
                negAt = i
                break

        if negAt == -1: return 0
        if n == 1:      return -1

        ofs = 1
        moves = 0
        allUsed = False

        while not allUsed and balance[negAt] < 0:
            l,r = (negAt-ofs+n)%n, (negAt+ofs)%n
            if abs(l-r) <= 1 or (l==0 and r==n-1):
                allUsed = True

            x = min(((balance[l] + balance[r]) if l!=r else balance[l]), -balance[negAt])
            moves += x*ofs
            balance[negAt] += x
            ofs += 1

        return moves if balance[negAt] >= 0 else -1