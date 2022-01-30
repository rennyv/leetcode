# Cheat Sheet

## DFS

def dfs(node):
    if not node: return

    #do stuff

    dfs(node.left)
    dfs(node.right)

dfs(root)

## BFS

def bfs(node):
    queue = []
    queue.append(node)

    while queue:
        item = queue.popleft()

        #do stuff
        
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

bfs(root)

## Trie
class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfString = False

class Trie:
    def __init__(self):
      self.root = TrieNode()

