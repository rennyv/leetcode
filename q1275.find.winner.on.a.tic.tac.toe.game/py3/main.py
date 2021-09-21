class Solution:
    def checkWin(self, m):
        win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for w in win:
            if w[0] in m and w[1] in m and w[2] in m:
                return True
        return False

    def tictactoe(self, moves):
        L = len(moves)

        i = 0
        turn = True
        A = []
        B = []
        while i < L and i < 9:
            val = moves[i][0] + (moves[i][1]*3)
            if turn:
                A.append(val)
                if self.checkWin(A) and len(A) > 2:
                    return 'A'
            else:
                B.append(val)
                if self.checkWin(B) and len(B) > 2:
                    return 'B'
            i += 1
            turn = not turn
        if L < 9: return 'Pending'
        return 'Draw'            

def test_ex1():
    moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    ans = 'A'

    sol = Solution()
    assert ans == sol.tictactoe(moves)

def test_ex4():
    moves = [[0,0],[1,1]]
    ans = "Pending"

    sol = Solution()
    assert ans == sol.tictactoe(moves)

test_ex4()