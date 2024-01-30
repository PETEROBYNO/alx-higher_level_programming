#!/usr/bin/python3
#101-nqueens.py
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_nqueens(board, col, N):
    if col == N:
        print_solution(board)
        return

    for row in range(N):
        if is_safe(board, row, col, N):
            board[col] = row
            solve_nqueens(board, col + 1, N)

def print_solution(board):
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)

def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

