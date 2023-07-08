chessBoard = [
    ["a", "R", "k", "B", "K", "Q", "B", "k", "R"],
    ["b", "P", "P", "P", "P", "P", "P", "P", "P"],
    ["c", " ", " ", " ", " ", " ", " ", " ", " "],
    ["d", " ", " ", " ", " ", " ", " ", " ", " "],
    ["e", " ", " ", " ", " ", " ", " ", " ", " "],
    ["f", " ", " ", " ", " ", " ", " ", " ", " "],
    ["g", "P", "P", "P", "P", "P", "P", "P", "P"],
    ["h", "R", "k", "B", "K", "Q", "B", "k", "R"]
]

def rowConverter(row):
    match endRow:
        case "a":
            endRow = 0
        case "b":
            endRow = 1
        case "c":
            endRow = 2
        case "d":
            endRow = 3
        case "e":
            endRow = 4
        case "f":
            endRow = 5
        case "g":
            endRow = 6
        case "h":
            endRow = 7
    return endRow

def moveRook(chessBoard, startingRow, startingCol):
    endRow = input("Enter the ending row: ")
    endCol = int(input("Enter the ending column: "))
    endRow = rowConverter(endRow)

    if startingRow == endRow: # if on same row
        if startingCol != endCol: # if on different columns
            for i in range(startingCol+1, endCol):
                if chessBoard[startingRow][i] != " ":
                    print("Invalid move")
                    return chessBoard
            chessBoard[startingRow][startingCol] = " "
            chessBoard[endRow][endCol] = "R"
            return chessBoard
    
    elif startingCol == endCol: # if on same column
        if startingRow != endRow: # if on different rows
            for i in range(startingRow+1, endRow):
                if chessBoard[i][startingCol] != " ":
                    print("Invalid move")
                    return chessBoard
            chessBoard[startingRow][startingCol] = " "
            chessBoard[endRow][endCol] = "R"
            return chessBoard