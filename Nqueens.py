

global N
N = int(input("Enter the number of queens: "))

def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def check(board, col):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if check(board, col + 1):
                return True
            board[i][col] = 0

    return False

def solveNQ():
    
    board =[]
    for i in range(N):
        k=[]
        for j in range(N):
            k.append(0)
        board.append(k)

    if check(board, 0) is False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

solveNQ()