
# Author : Amol Ambkar
# Problem : 8 Queen Problem using Backtracking
 

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print (board[i][j], end = " ")
        print()

def safe(board, row, col):
  
    for i in range(col):
        if board[row][i] == 1:
            return False
  
    for i, j in zip(range(row, -1, -1), 
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
  
    for i, j in zip(range(row, N, 1), 
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
  
    return True
  
def solve(board, col):
    
    if col >= N:
        return True
  
    for i in range(N):
  
        if safe(board, i, col):
            board[i][col] = 1
  
            if solve(board, col + 1) == True:
                return True
  
            board[i][col] = 0
    return False
      
def solveNQ():
    board = []
    for i in range(N):
        l = [0]*N
        board.append(l)

    if (solve(board, 0) == False):
        print("Solution does not exist")
        return False
    printSolution(board)
    return True
      
global N
N = int(input("Enter N : "))

solveNQ() 
