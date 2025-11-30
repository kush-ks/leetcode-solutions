import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        n = len(points)
        rem = n
        heap = []
        cost = 0

        heapq.heappush(heap,[0,0])

        while rem > 0:
            d,i = heapq.heappop(heap)
            if i in visited:
                continue
            cost += d
            visited.add(i)
            rem -= 1

            for j in range(n):
                if j not in visited:
                    dist = abs(points[j][0]-points[i][0]) + abs(points[j][1]-points[i][1])
                    heapq.heappush(heap,[dist,j])
        
        return cost