import re

import numpy as np


def is_marked(cell):
    return cell[1]


def cell_score(cell):
    if is_marked(cell):
        return 0
    return cell[0]


def read_input():
    with open('day4.input') as f:
        parts = f.read().strip().split('\n\n')
    numbers = np.array([int(n) for n in parts[0].split(',')])
    boards = np.array(
        [[[(int(n), False) for n in re.split(r'\s+', line.strip())] for line in board.split('\n')] for board in
         parts[1:]]
    )
    return numbers, boards


def get_winning_boards(boards, n):
    to_mark = np.all(np.equal(boards, (n, False)), 3)
    boards[to_mark] = (n, True)
    marked_cells = np.apply_along_axis(is_marked, 3, boards)
    winning_rows = np.all(marked_cells, 2)
    marked_cells_t = np.transpose(marked_cells, (0, 2, 1))
    winning_columns = np.all(marked_cells_t, 2)
    winning_boards = np.logical_or(np.any(winning_rows, 1), np.any(winning_columns, 1))
    return winning_boards


def day4a():
    numbers, boards = read_input()
    winning_board = None
    winning_number = None
    for n in numbers:
        winning_boards = get_winning_boards(boards, n)
        if np.any(winning_boards):
            winning_board = boards[winning_boards]
            winning_number = n
            break
    score = np.sum(np.apply_along_axis(cell_score, 3, winning_board))
    return score * winning_number


def day4b():
    numbers, boards = read_input()
    final_number = None
    for n in numbers:
        winning_boards = get_winning_boards(boards, n)
        if boards.shape[0] > 1:
            boards = boards[np.logical_not(winning_boards)]
        if np.all(winning_boards):
            final_number = n
            break
    score = np.sum(np.apply_along_axis(cell_score, 3, boards))
    return score * final_number


if __name__ == '__main__':
    print(day4a())
    print(day4b())
