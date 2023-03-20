import numpy as np


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def test():
        print(bcolors.HEADER + "HEADER" + bcolors.ENDC)
        print(bcolors.OKBLUE + "OKBLUE" + bcolors.ENDC)
        print(bcolors.OKCYAN + "OKCYAN" + bcolors.ENDC)
        print(bcolors.OKGREEN + "OKGREEN" + bcolors.ENDC)
        print(bcolors.WARNING + "WARNING" + bcolors.ENDC)
        print(bcolors.FAIL + "FAIL" + bcolors.ENDC)
        print(bcolors.ENDC + "ENDC" + bcolors.ENDC)
        print(bcolors.BOLD + "BOLD" + bcolors.ENDC)
        print(bcolors.UNDERLINE + "UNDERLINE" + bcolors.ENDC)


# bcolors.test()


def print_sudoku(sudoku, puzzle: list = None):
    for row in range(9):
        for colum in range(9):
            if puzzle is not None and puzzle[row][colum] != 0:
                print(bcolors.OKGREEN + str(sudoku[row, colum]) + bcolors.ENDC, end=" ")
            else:
                print(bcolors.HEADER + str(sudoku[row, colum]) + bcolors.ENDC, end=" ")
            if (colum + 1) % 3 == 0 and (colum + 1) < 9:
                print("|", end=" ")
        print()
        if (row + 1) % 3 == 0 and (row + 1) < 9:
            print("- " * 11)


def solve_sudoku(puzzle: list):
    """Функція для вирішення судоку"""
    # перевірка розмірності матриці
    if len(puzzle) != 9 or len(puzzle[0]) != 9:
        raise ValueError("Розмір матриці повинен бути 9x9")

    # копіюємо матрицю для уникнення змін у вхідному пазлі
    grid = np.array(puzzle)

    # рекурсивно заповнюємо матрицю
    solve_cell(0, 0, grid)

    # повертаємо вирішений пазл
    return grid.tolist()


def solve_cell(row, col, grid):
    """Функція для рекурсивного заповнення клітинок"""
    # якщо заповнення досягло кінця рядка, перехід на наступний рядок
    if col == 9:
        row += 1
        col = 0

        # якщо заповнення досягло кінця матриці, пазл вирішено
        if row == 9:
            return True

    # якщо клітина вже заповнена, перехід до наступної клітини
    if grid[row][col] != 0:
        return solve_cell(row, col + 1, grid)

    # перебір можливих значень для клітини
    for val in range(1, 10):
        # перевірка, чи можна вставити значення в клітину
        if check_valid(row, col, val, grid):
            # вставка значення
            grid[row][col] = val

            # рекурсивне заповнення наступної клітини
            if solve_cell(row, col + 1, grid):
                return True

            # якщо рекурсивне заповнення наступної клітини не дало результатів,
            # знову встановлюємо значення клітини в 0 і повертаємося назад
            grid[row][col] = 0

    # якщо ні одне значення не може бути вставлене в клітину, повертаємося назад
    return False


def check_valid(row, col, val, grid):
    """Функція для перевірки чи можна вставити значення в клітину"""
    # перевірка рядка
    if val in grid[row, :]:
        return False

    # перевірка стовпця
    if val in grid[:, col]:
        return False

    # перевірка квадрата
    square_row = (row // 3) * 3
    square_col = (col // 3) * 3
    if val in grid[square_row:square_row + 3, square_col:square_col + 3]:
        return False

    # якщо жодна перевірка не виявила конфлікт, значення можна вставити в клітину
    return True


if __name__ == '__main__':
    puzzle = [
        [0, 0, 0,   0, 8, 0,   9, 0, 2],
        [8, 0, 0,   7, 0, 0,   0, 6, 5],
        [0, 0, 0,   0, 0, 0,   3, 0, 0],

        [0, 0, 0,   4, 0, 0,   0, 0, 8],
        [9, 0, 0,   0, 3, 0,   0, 0, 1],
        [1, 0, 0,   0, 0, 8,   0, 0, 0],

        [0, 0, 6,   0, 0, 0,   0, 0, 0],
        [3, 8, 0,   0, 0, 7,   0, 0, 0],
        [4, 0, 5,   0, 1, 0,   0, 0, 0]
    ]

    solved_puzzle = solve_sudoku(puzzle)
    print(bcolors.WARNING + f"{'Solved Sudoku!':^21}" + bcolors.ENDC)
    print_sudoku(np.matrix(solved_puzzle), puzzle)
