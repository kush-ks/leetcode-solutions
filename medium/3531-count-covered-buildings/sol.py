from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        hor,ver = defaultdict(tuple), defaultdict(tuple)
        covered = 0

        for a,b in buildings:
            if a in ver: ver[a] = ( min(ver[a][0],b), max(ver[a][1],b) )
            else:        ver[a] = ( b, b )
            if b in hor: hor[b] = ( min(hor[b][0],a), max(hor[b][1],a) )
            else:        hor[b] = ( a, a )
        
        for a,b in buildings:
            if (hor[b][0] < a < hor[b][1]) and (ver[a][0] < b < ver[a][1]):
                covered += 1

        return covered