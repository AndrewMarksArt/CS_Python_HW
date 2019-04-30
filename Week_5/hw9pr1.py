# hw9pr1.py
# Andrew Marks

import random
from copy import deepcopy


def createOneRow(width):
    """
    Returns on row of zeros of width "width".
    You might use this in your createBoard (width, height) function.
    :param width:
    :return:
    """
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoard(width, height):
    """
    Create the board of width x height
    :param width: int
    :param height: int
    :return: list of lists to create the board for conways game of life
    """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard(A):
    """
    Takes the board that was created and prints it out
    :param A: a list of rows and columns
    :return: prints out the board
    """
    for row in A:
        print()
        for col in row:
            print(col, end='')


def diagonalize(width, height):
    """
    creates a list of lists that can be used to create a board for the game with all 0s and a diagonal row of 1s
    :param width: int
    :param height: int
    :return: List of list, each list in the list A will have a len of width and there will be height number of lists
    """
    A = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A


def innerCells(w, h):
    """
    Creates a list of lists used to create a board, with the outer edge as 0s and the middle cells all 1s
    :param w: int
    :param h: int
    :return: A, list of lists, the number of the lists in A will be h elements long
    and each element is a list w elements long
    """
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if row == row:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A


def randomCells(w, h):
    """
    Creates a list of lists used to make the board, the board will have edges of all 0s and the inner cells will
    be 1s or 0s randomly
    :param w: int
    :param h: int
    :return: A, list of lists, the number of the lists in A will be h elements long
    and each element is a list w elements long
    """
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if row == row:
                A[row][col] = random.choice([0, 1])
            else:
                A[row][col] = 0
    return A


def copy(A):
    """
    creates a copy of the board that will be changed for the next generation of the game
    :param A: List
    :return: copy of the List
    """
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            newA[row][col] = A[row][col]

    return newA


def innerReverse(A):
    """
    Takes a list, reverses the inner cells leaving the edges as 0s
    :param A: List
    :return: New List, copy of list A but with inner cells reversed
    """
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == row:
                if A[row][col] == 1:
                    newA[row][col] = 0
                else:
                    newA[row][col] = 1
            else:
                newA[row][col] = 0

    return newA


def countNeighbors(row, col, A):
    """
    Takes a List A and counts the neighboring cells of those that are 1s
    :param row: int
    :param col: int
    :param A: List
    :return: the count of the neighboring cells of 1s
    """
    count = 0
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if x == 0 and y == 0:
                count += 0
            else:
                if A[row + x][col + y] == 1:
                    count += 1

    return count


def next_life_generation(A):
    """
    updates the board for the next generation according to the game of life rules
    :param A: List
    :return: List, a new board that is the next generation of the game of life
    """
    newA = copy(A)
    height = len(A)
    width = len(A[0])

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == row:
                if countNeighbors(row, col, A) < 2:
                    newA[row][col] = 0
                if countNeighbors(row, col, A) > 3:
                    newA[row][col] = 0
                if countNeighbors(row, col, A) == 3:
                    newA[row][col] = 1
            else:
                newA[row][col] = 0

    return newA



