from cgi import test
from collections import defaultdict
from typing import List 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(set)

        for e in edges:
            start, end = e
            g[start].add(end)
            g[end].add(start)

        has_cycle=False
        visited=set()
        
        def dfs(node, parent):
            nonlocal has_cycle
            visited.add(node)

            for n in g[node]:
                if n in visited and not n  in [node, parent]:
                    has_cycle = True
                elif not n in visited:
                   dfs(n, node)
        dfs(0, None)
        
        return not has_cycle and len(visited)==n


def test_ex1():
    n = 5
    edges = [[0,1],[0,2],[0,3],[1,4]]

    sol = Solution()
    assert sol.validTree(n, edges)


def test_ex2():
    n = 5
    edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]

    sol = Solution()
    assert not sol.validTree(n, edges)

test_ex2()
