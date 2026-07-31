N = 8

# Print the board
def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

# Check if safe to place queen
def is_safe(board, row, col):
    # Check left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True

# Solve using backtracking
def solve(board, col):
    if col >= N:
        print_board(board)
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve(board, col + 1):
                return True

            board[i][col] = 0  # Backtrack

    return False

# Main execution
board = [[0 for _ in range(N)] for _ in range(N)]

if not solve(board, 0):
    print("No solution exists")
