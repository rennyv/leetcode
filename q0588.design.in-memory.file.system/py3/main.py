from typing import List

class TrieNode:
    def __init__(self):
        self.is_file = False
        self.children = {}
        self.content = None

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        node = self.get_node(path)
        if node.is_file:
            return [self.split_path(path)[-1]]
        return sorted(node.children.keys())        

    def mkdir(self, path: str) -> None:
        node = self.put_node(path)
        node.is_file = False                

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.put_node(filePath)
        node.is_file = True
        node.content = node.content + content if node.content else content

    def readContentFromFile(self, filePath: str) -> str:
        return self.get_node(filePath).content

    def get_node(self, path):
        node = self.root
        for dir in self.split_path(path):
            node = node.children[dir]
        return node

    def put_node(self, path):
        node = self.root
        for dir in self.split_path(path):
            if dir not in node.children:
                node.children[dir] = TrieNode()
            node = node.children[dir]
        return node
    
    def split_path(self, path):
        if path == "/":
            return []
        return path[1:].split('/')


def test_ex1():
    fs = FileSystem()
    assert [] == fs.ls("/")
    fs.mkdir("/a/b/c")
    fs.addContentToFile("/a/b/c/d", "hello")
    assert ["a"] == fs.ls("/")
    assert "hello" == fs.readContentFromFile("/a/b/c/d")  


test_ex1()