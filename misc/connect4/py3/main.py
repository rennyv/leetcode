def connect4():
    #create board
    rows = 6
    columns = 7
    board = [[ "-" for _ in range(columns)] for _ in range(rows)]
    rowIdx = [0 for _ in range(columns)]

    current_turn = 1

    while True:
        player = "O" if current_turn % 2 else "X"

        y = int(input("Player %s turn, pick a column: " % player))
        
        
        if 0 <= y and y < columns and rowIdx[y] < rows:
            x = rowIdx[y]

            board[x][y] = player
            rowIdx[y] += 1
        else:
            print("Invalid Column try again")
            continue

        if checkWinning(board, x, y, player, rows, columns):
            print("Player %s, won in %s turns!" % (player, current_turn))
            break
        current_turn += 1

        if current_turn > rows*columns:
            print("Tie Game")
            break




def checkWinning(board, x, y, player, rows, columns):
    for r in board[::-1]:
       print(r)
    print("\n")
            # (left, right), (Up, down)    
    tests = [((0,1),(0,-1)), ((1,0),(-1,0)), ((1,1),(-1,-1)), ((-1,1), (1,-1))]

    for test in tests:
        connected = 0
        tx, ty = x, y
        for i in test:            
            while 0 <= tx < rows and 0 <= ty < columns and board[tx][ty] == player:
                connected += 1
                tx += i[0]
                ty += i[1]
            tx, ty = x, y
        if connected > 4:
            return True
    return False

connect4()