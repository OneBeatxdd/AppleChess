# board for function chessboard, marks for marks_grid, one for the side represents by 1, negaOne for the side of -1
def init_chessboard(board):
    board[3][3] = 1
    board[3][4] = -1
    board[4][3] = -1
    board[4][4] = 1


def print_board(board):             # TODO: change this to print to the UI
    for i in range(0, 8):
        for j in range(0, 8):
            print(board[i][j], end="  ")
        print()
    print()


# TODO: (THIS IS FOR AI) update score grid * board    DEBUG STAGE
def update_score(board, marks):
    one, negaOne = 0, 0, 0, 0
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == 1:
                one += marks[i][j]
            elif board[i][j] == -1:
                negaOne += marks[i][j]
    return one, negaOne


# TODO: count the board pieces
def count_pieces(board):
    one, negaOne = 0, 0, 0, 0
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == 1:
                one += 1
            elif board[i][j] == -1:
                negaOne += 1
    return one, negaOne


def print_score(one, negaOne, onePiece, negaPiece):
    print("My Score: ", one, "Opponent Score: ", negaOne)
    print("My Piece: ", onePiece, "Opponent Piece: ", negaPiece)
    print()


# TODO: check if the available move for the side
def available_moves(side, board):
    availableMovesList = []                     # (actualMovement, originalPosition, position)
    checkedPositionList = []
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == side:
                loop = 0
                checkedPositionList.append((i, j))
                for x in range(1, 9):
                    moves = check_around(side, (i, j), x, board, loop)
                    if moves:
                        #if not empty
                        availableMovesList.append((moves, (i, j), x))
    return availableMovesList


def check_around(side, originalPosition, checkPosition, board, iteration):
    row, col = originalPosition[0], originalPosition[1]
    if checkPosition == 1:
        if row == 0 or col == 0:
            return []
        else:
            if board[row-1][col-1] == side:
                return []
            elif board[row-1][col-1] == 0:
                if iteration > 0:
                    return (row-1, col-1)
                return []
            else:           # opposite side
                iteration += 1
                return check_around(side, (row-1, col-1), 1, board, iteration)
    elif checkPosition == 2:
        if row == 0:
            return []
        else:
            if board[row-1][col] == side:
                return []
            elif board[row-1][col] == 0:
                if iteration > 0:
                    return (row-1, col)
                return []
            else:
                iteration += 1
                return check_around(side, (row-1, col), 2, board, iteration)
    elif checkPosition == 3:
        if row == 0 or col == 7:
            return []
        else:
            if board[row-1][col+1] == side:
                return []
            elif board[row-1][col+1] == 0:
                if iteration > 0:
                    return (row-1, col+1)
                return []
            else:
                iteration += 1
                return check_around(side, (row-1, col+1), 3, board, iteration)
    elif checkPosition == 4:
        if col == 0:
            return []
        else:
            if board[row][col-1] == side:
                return []
            elif board[row][col-1] == 0:
                if iteration > 0:
                    return (row, col-1)
                return []
            else:
                iteration += 1
                return check_around(side, (row, col-1), 4, board, iteration)
    elif checkPosition == 5:
        if col == 7:
            return []
        else:
            if board[row][col+1] == side:
                return []
            elif board[row][col+1] == 0:
                if iteration > 0:
                    return (row, col+1)
                return []
            else:
                iteration += 1
                return check_around(side, (row, col+1), 5, board, iteration)
    elif checkPosition == 6:
        if row == 7 or col == 0:
            return []
        else:
            if board[row+1][col-1] == side:
                return []
            elif board[row+1][col-1] == 0:
                if iteration > 0:
                    return (row+1, col-1)
                return []
            else:
                iteration += 1
                return check_around(side, (row+1, col-1), 6, board, iteration)
    elif checkPosition == 7:
        if row == 7:
            return []
        else:
            if board[row+1][col] == side:
                return []
            elif board[row+1][col] == 0:
                if iteration > 0:
                    return (row+1, col)
                return []
            else:
                iteration += 1
                return check_around(side, (row+1, col), 7, board, iteration)
    elif checkPosition == 8:
        if row == 7 or col == 7:
            return []
        else:
            if board[row+1][col+1] == side:
                return []
            elif board[row+1][col+1] == 0:
                if iteration > 0:
                    return (row+1, col+1)
                return []
            else:
                iteration += 1
                return check_around(side, (row+1, col+1), 8, board, iteration)


# TODO: confirm the move and change the chessboard
def actual_move(board, choice):
    side = board[choice[1][0]][choice[1][1]]
    direction = choice[2]
    origRow, origCol = choice[1][0], choice[1][1]
    destRow, destCol = choice[0][0], choice[0][1]
    while not (origRow == destRow and origCol == destCol):
        if direction == 1:
            origRow -= 1
            origCol -= 1
        elif direction == 2:
            origRow -= 1
        elif direction == 3:
            origRow -= 1
            origCol += 1
        elif direction == 4:
            origCol -= 1
        elif direction == 5:
            origCol += 1
        elif direction == 6:
            origRow += 1
            origCol -= 1
        elif direction == 7:
            origRow += 1
        elif direction == 8:
            origRow += 1
            origCol += 1
        board[origRow][origCol] = side


# TODO: link the UI to the input i think


def user_move(board):
    # TODO: generate the move list for user to put in
    choices = available_moves(1, board)
    if not choices:         # if empty
        print("You dun have any available moves hence passing you here")
        input("Press Enter to continue...")
        pass
    for choice in choices:
        print("(actualMovement, originalPosition, position)", choice[0], choice[1], choice[2])

    valid = False
    while not valid:
        # TODO: get user input for the move NOW terminal but later get it from UI
        userMove[0], userMove[1] = input("Enter coordinate: ").split()
        userCoordinates = (int (userMove[0]), int (userMove[1]))
        print(userCoordinates)
        userChosenMove = []
        # check if valid
        for choice in choices:
            if choice[0] == userCoordinates:
                userChosenMove.append(choice)
                valid = True
        if not valid:
            print("Please enter again cuz this is an invalid move")

    # check if the moves are more 1 directions
    for move in userChosenMove:
        # TODO: make the actual move
        actual_move(board, move)


# main
if __name__ == '__main__':
    myScore, oppoScore = 0, 0
    myPiece, oppoPiece = 0, 0
    w, h = 8, 8
    userMove = [0, 0]

    chessboard = [[0 for x in range(w)] for y in range(h)]    # the chessboard for user to actually see
    marks_grid = [[5,3,4,4,4,4,3,5],
                  [3,2,3,3,3,3,2,3],
                  [4,3,1,1,1,1,3,4],
                  [4,3,1,1,1,1,3,4],
                  [4,3,1,1,1,1,3,4],
                  [4,3,1,1,1,1,3,4],
                  [3,2,3,3,3,3,2,3],
                  [5,3,4,4,4,4,3,5]]     # the marks for AI to take
    init_chessboard(chessboard)

    # DEBUG
    print_board(chessboard)
    print_board(marks_grid)
    myScore, oppoScore = update_score(chessboard, marks_grid)
    myPiece, oppoPiece = count_pieces(chessboard)
    print_score(myScore, oppoScore, myPiece, oppoPiece)
    # DEBUG

    # TODO: loop like while there is still choice to move for both ppl
    turn = 1  # turn 1 or -1 who is going to move 0 = end both
    # user moving the piece
    user_move(chessboard)
    print_board(chessboard)

    # AI turn or -1 turn
    turn = -1

    # TODO: make the actual move