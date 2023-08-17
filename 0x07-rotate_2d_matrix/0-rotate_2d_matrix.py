#!/usr/bin/python3
"""
    Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
        rotate a n * n matrix
    """
    lent = len(matrix)
    for i in range(lent):
        for j in range(i, lent):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(lent):
        matrix[i].reverse()
