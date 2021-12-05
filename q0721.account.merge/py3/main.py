# DFS
from typing import List

class Solution:
    def dfs(self, node, graph, visited, component):
        if visited[node]:
            return
        
        visited[node] = True
        component.append(node)
        for neighbour in graph[node]:
            if not visited[neighbour]:
                self.dfs(neighbour, graph, visited, component)
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        visited = {}
        email_to_account = {}

        #set up graph
        for account in accounts:
            emails = account[1:]
            first_email = emails[0]
            for email in emails:
                graph.setdefault(email, set()).add(first_email)
                graph.setdefault(first_email, set()).add(email)
                visited[email] = False
                email_to_account[email] = account[0]

        output = []
        for email, account in email_to_account.items():
            if visited[email]:
                continue
            nodes = []
            self.dfs(email, graph, visited, nodes)
            output.append([account] + sorted(nodes))

        return output