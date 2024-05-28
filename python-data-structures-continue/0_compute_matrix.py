#!/usr/bin/python3
def compute_matrix(matrix=[]):
    squared_matrix = []

    for row in matrix:
        squared_row = []
        for element in row:
            squared_row.append(element * element)
        squared_matrix.append(squared_row)

    return squared_matrix


if __name__ == "__main__":
    matrix = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    print(f"Original: {matrix}")
    print(f"Modified: {compute_matrix(matrix)}")
