def get_user_input():
    n =int(input("enter the number of rows/columns of the board:"))
    queens = int(input("enter the number of queens:"))

    if queens > n:
        print("number of queens can not exceed the board size!")
        return None, None
    
    return n, queens

def is_safe(board, row, col):
    for i in range (row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_queens ( n, queens, board, row=0, solutions = []):
    if row == queens:
        solutions.append(board[ : ])
        return
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(n, queens, board, row +1, solutions)
            board [row] = -1

def print_board(board, n):
    for row in range(len(board)):
        line = ""
        for col in range (n):
            line += " 0 " if board[row]== col else " . "
        print(line)
    print()

def main():
    n, queens = get_user_input()
    if n is None or queens is None:
        return
    

    board = [-1]*n
    solutions = []

    solve_queens(n, queens, board, 0, solutions)
    
    print(f"\nnumber of solutions for {queens} queens on a{n}x{n} board: {len (solutions)}")
    for idx in range(len(solutions)):
        print("\nsolution" + str(idx + 1) + ":")
        print_board(solutions[idx], n)