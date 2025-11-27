class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        bulls, cows = 0, 0
        c = [0 for _ in range(10)]
        
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                a,b = int(secret[i]), int(guess[i]) 
                if c[a]>0: cows += 1
                if c[b]<0: cows += 1
                c[a] -= 1
                c[b] += 1

        return f"{bulls}A{cows}B"