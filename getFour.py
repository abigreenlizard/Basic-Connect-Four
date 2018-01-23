BOARDHEIGHT = 6
BOARDWIDTH = 7

def main():
    GAMEOVER = False
    GAMECOUNTER = 0
    board = createNewBoard()
    printBoard(board)

    while not GAMEOVER:
        GAMECOUNTER += 1
        if GAMECOUNTER % 2 == 0:
            player = 'R'
        else:
            player = 'Y'
        print('{}\'s turn'.format(player))
        move = int(input('Enter move  ~'))
        while not isMoveLegal(move, board):
            print('illegal move')
            move = int(input('Enter move  ~'))
        makeMove(move, board, player)
        printBoard(board)
        if isWinningMove(board, player):
            print(player, 'got connect four!')
            GAMEOVER = True

def createNewBoard():
    board = []
    for i in range(BOARDHEIGHT):
        board.append(['O'] * BOARDWIDTH)
    return board

def printBoard(board):
    for i in board:
        print(i, '\n')

def isMoveLegal(move, board):
    if not (move >= 0 and move <= 6):
        return False
    for row in board:
        if row[move]=='O':
            return True
    return False

def makeMove(move, board, player):
    for row in board[::-1]:
        if row[move]=='O':
            row[move]=player
            break

def isWinningMove(board, player):
    # horizontal win
    for x in range(BOARDHEIGHT):
        for y in range(BOARDWIDTH-3):
            if board[x][y]==player and board[x][y+1]==player and board[x][y+2]==player and board[x][y+3]==player:
                return True
    # vertical win
    for x in range(BOARDHEIGHT-3):
        for y in range(BOARDWIDTH):
            if board[x][y] == player and board[x+1][y] == player and board[x+2][y] == player and board[x+3][y] == player:
                return True
    # diagonal \ win
    for x in range(BOARDHEIGHT-3):
        for y in range(BOARDWIDTH-3):
            if board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player and board[x+3][y+3] == player:
                return True
    #diagonal / win
    for x in range(BOARDHEIGHT-3):
        for y in range(3, BOARDWIDTH):
            if board[x][y] == player and board[x+1][y-1] == player and board[x+2][y-2] == player and board[x+3][y-3] == player:
                return True
    return False

#board = createNewBoard()
#printBoard(board)

main()
