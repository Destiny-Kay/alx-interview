#!/usr/bin/python3
"""
A solution for the N-queens problem
"""
import sys


def nqueens(N):
    """
    Returns all the possible ways N number of queens can be
    arranged on a chessboard
    without any queen attacking another.

    Args:
        N: Size of the chessboard and the number of queens.

    Returns:
        List of solutions, each solution is a list of queen positions.
    """
    solutions = []
    solve_n_queens(N, 0, [], solutions)
    return solutions


def solve_n_queens(N, row, current_solution, solutions):
    """
    A utility function to solve the problem.

    Args:
        N: Size of the chessboard and the number of queens.
        row: Current row to place the queen.
        current_solution: List of current positions of queens.
        solutions: List to store all valid solutions.
    """
    if row == N:
        solutions.append(current_solution.copy())
        return
    for col in range(N):
        if is_safe(row, col, current_solution):
            current_solution.append((row, col))
            solve_n_queens(N, row + 1, current_solution, solutions)
            current_solution.pop()


def is_safe(row, col, current_solution):
    """
    Checks whether a queen is under attack in a particular cell on the board.

    Args:
        row: Row to be checked.
        col: Column to be checked.
        current_solution: List of current positions of queens.

    Returns:
        True if the position is safe, otherwise False.
    """
    for queen_row, queen_col in current_solution:
        if queen_row == row or queen_col == col or \
         abs(queen_row - row) == abs(queen_col - col):
            return False
    return True


def print_solutions(solutions):
    """
    Prints all the solutions in the required format.

    Args:
        solutions: List of solutions to be printed.
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    argN = sys.argv[1]

    if not argN.isdigit():
        print("N must be a number")
        exit(1)
    N = int(argN)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    solutions = nqueens(N)
    print_solutions(solutions)
