class Solution:
    def timeRound(self, t:int, ceil:bool) -> int:
        rem = t % 15
        if rem == 0: return t
        if ceil: return t+(15-rem) if t+(15-rem) < 24*60 else 0
        return t-rem

    
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        inArr = loginTime.split(":")
        outArr = logoutTime.split(":")

        hIn, mIn = int(inArr[0]), int(inArr[1])
        hOut, mOut = int(outArr[0]), int(outArr[1])

        inTime = self.timeRound(hIn*60 + mIn, True)
        outTime = self.timeRound(hOut*60 + mOut, False)

        rounds = 0

        if not 0 < (hOut*60 + mOut - hIn*60 - mIn) < 15:
            if inTime <= outTime:
                rounds = (outTime - inTime) // 15
            else:
                rounds = (24*60 - (inTime - outTime)) // 15
        

        return rounds