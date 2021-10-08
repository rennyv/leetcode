from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        c = 0
        
        def find(i,j,c):
            if c == len(word): return True
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[c]: return False
            board[i][j] = 0
            if find(i,j+1,c+1) or find(i+1,j,c+1) or find(i,j-1,c+1) or find(i-1,j,c+1): return True
            board[i][j] = word[c]
            
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and find(i,j,c): return True
        return False


        for i in range(m):
            for j in range(n):
                u = set()
                findWord(0, i,j, u)


def test_ex1():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"

    sol = Solution()
    assert sol.exist(board, word)

def test_ex2():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"

    sol = Solution()
    assert sol.exist(board, word)


def test_ex3():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"

    sol = Solution()
    assert not sol.exist(board, word)

test_ex1()