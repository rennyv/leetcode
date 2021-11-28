from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(path):
            if path[-1] == len(graph)-1: ans.append(path)
            else:
                for child in graph[path[-1]]:
                    dfs(path + [child])
        dfs([0])
        return ans