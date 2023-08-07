chessBoard = [
    ["a", "R", "k", "B", "K", "Q", "B", "k", "R"],
    ["b", "P", "P", "P", "P", "P", "P", "P", "P"],
    ["c", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["d", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["e", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["f", "_", "_", "_", "P", "_", "_", "_", "_"],
    ["g", "P", "P", "P", "_", "P", "P", "P", "P"],
    ["h", "R", "k", "B", "K", "Q", "B", "k", "R"]
]

def printBoard(board):
    print("-------------------------")
    i = 0
    while i < len(board):
        j = 0
        while j < len(board[i]):
            print(board[i][j], end="|")
            if j == 8:
                print()
            j += 1
        i += 1
    print("-------------------------")
    print(" 1 2 3 4 5 6 7 8")

def rowConverter(row):
    match row:
        case "a":
            row = 0
        case "b":
            row = 1
        case "c":
            row = 2
        case "d":
            row = 3
        case "e":
            row = 4
        case "f":
            row = 5
        case "g":
            row = 6
        case "h":
            row = 7
    return row

def moveRook(chessBoard, startingRow, startingCol):
    endRow = input("Enter the ending row: ")
    endCol = int(input("Enter the ending column: "))
    endRow = rowConverter(endRow)

    if startingRow == endRow: # if on same row
        if startingCol != endCol: # if on different columns
            for i in range(startingCol+1, endCol): # loop through all the columns on the starting row
                if chessBoard[startingRow][i] != "_": # if there is a piece in the way
                    print("Invalid move")
                    return 1
            chessBoard[startingRow][startingCol] = "_" # remove the piece from the starting position
            chessBoard[endRow][endCol] = "R" # place the piece in the ending position
            return chessBoard
    
    elif startingCol == endCol: # if on same column
        if startingRow != endRow: # if on different rows
            for i in range(startingRow+1, endRow): # loop through all the rows on the starting column
                if chessBoard[i][startingCol] != "_": # if there is a piece in the way
                    print("Invalid move")
                    return 1
            chessBoard[startingRow][startingCol] = "_" # remove the piece from the starting position
            chessBoard[endRow][endCol] = "R" # place the piece in the ending position
            return chessBoard
        
    print("Invalid move")
    return 1


def moveBishop(chessBoard, startingRow, startingCol):
    endRow = rowConverter(input("Enter the ending row: "))
    endCol = int(input("Enter the ending column: "))

    if abs(startingRow - endRow) == abs(startingCol - endCol): # if the difference between the starting and ending row is the same as the difference between the starting and ending column

        if startingRow < endRow and startingCol < endCol: # if the ending position is in the bottom right quadrant
            for i in range(startingRow+1, endRow): # loop through all the rows between the starting and ending position
                if chessBoard[i][i] != "_": # if there is a piece in the way
                    print("Invalid move")
                    return 1
            chessBoard[startingRow][startingCol] = "_" # remove the piece from the starting position
            chessBoard[endRow][endCol] = "B" # place the piece in the ending position
            return chessBoard
        
        elif startingRow < endRow and startingCol > endCol: # if the ending position is in the bottom left quadrant
            for i in range(startingRow+1, endRow): # loop through all the rows between the starting and ending position
                if chessBoard[i][-i] != "_": # if there is a piece in the way
                    print("Invalid move")
                    return 1
            chessBoard[startingRow][startingCol] = "_" # remove the piece from the starting position
            chessBoard[endRow][endCol] = "B" # place the piece in the ending position
            return chessBoard
        
        elif startingRow > endRow and startingCol < endCol: # if the ending position is in the top right quadrant
            for i in range(startingCol+1, endCol+1): # loop through all the rows between the starting and ending position
                if chessBoard[-i][i] != "_": # if there is a piece in the way
                    print("Invalid move")
                    return 1
            chessBoard[startingRow][startingCol] = "_" # remove the piece from the starting position
            chessBoard[endRow][endCol] = "B" # place the piece in the ending position
            return chessBoard
        
        elif startingRow > endRow and startingCol > endCol: # if the ending position is in the top left quadrant
            for i in range(endCol, startingCol-1): # loop through all the rows between the starting and ending position
                if chessBoard[-i][-i] != "_": # if there is a piece in the way
                    print("Invalid move")
                    return 1
            chessBoard[startingRow][startingCol] = "_" # remove the piece from the starting position
            chessBoard[endRow][endCol] = "B" # place the piece in the ending position
            return chessBoard
        
    print("Invalid move")
    return 1

def moveKnight(chessBoard, startingRow, startingCol):
    endRow = rowConverter(input("Enter the ending row: "))
    endCol = int(input("Enter the ending column: "))

    if (abs(startingRow - endRow) == 2 and abs(startingCol - endCol) == 1) or (abs(startingRow - endRow) == 1 and abs(startingCol - endCol) == 2): # if the difference between the starting and ending row is 2 and the difference between the starting and ending column is 1 or vice versa
        chessBoard[startingRow][startingCol] = "_"
        chessBoard[endRow][endCol] = "k"
        return chessBoard
    
    print("Invalid move")
    return 1