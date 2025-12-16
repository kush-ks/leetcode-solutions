class Solution:
    def numberOfWays(self, corridor: str) -> int:
        ways = 1
        MOD = pow(10,9)+7
        start = -1

        for i in range(len(corridor)):
            if corridor[i] == 'S':
                start = i
                break

        if start == -1:
            return 0

        paired = True
        buff = 0

        for i in range(start, len(corridor)):
            if corridor[i] == 'P':
                if paired: buff += 1
            else:
                if paired: 
                    ways = (ways * (buff + 1)) % MOD
                    buff = 0
                paired = not paired


        return ways if paired else 0