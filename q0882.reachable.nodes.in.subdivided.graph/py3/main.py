from typing import DefaultDict
import sys
from heapq import heappop, heappush

class Solution:
    def reachableNodes(self, edges, maxMoves, n) -> int:
        graph = DefaultDict(list)
        for u,v,w in edges:
            graph[u].append((v, w+1))
            graph[v].append((u,w+1))
        
        dist = [sys.maxsize] * n 
        dist[0] = 0

        pq = [(0,0)] #current distance to node u

        while pq:
            d,u = heappop(pq)

            for v,nd in graph[u]:
                if d + nd < dist[v]:
                    dist[v] = d + nd
                    heappush(pq, (d+nd,v))

        ans = 0
        for u,w in enumerate(dist):
            if dist[u] <= maxMoves:
                ans += 1

        for u,v,w in edges:
            if dist[u] > maxMoves and dist[v] > maxMoves:
                continue

            cnt1 = max(maxMoves-dist[u],0)
            cnt2 = max(maxMoves-dist[v],0)

            ans += min(cnt1+cnt2, w)
        
        return ans


        


def test_ex1():
    edges = [[0,1,10],[0,2,1],[1,2,2]]
    maxMoves = 6
    n = 3
    ans = 13

    sol = Solution()
    assert ans == sol.reachableNodes(edges, maxMoves, n)

def test_ex2():
    edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]]
    maxMoves = 10
    n = 4
    ans = 23

    sol = Solution()
    assert ans == sol.reachableNodes(edges, maxMoves, n)

def test_ex3():
    edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]]
    maxMoves = 17
    n = 5
    ans = 1

    sol = Solution()
    assert ans == sol.reachableNodes(edges, maxMoves, n)

test_ex1()