#!/usr/bin/python3
"""
Function to create a pascal triangle
"""


def pascal_triangle(n):
    """
    A function that computes and return a pascal triangle

    """
    # create outerlist
    outerList = []
    if n <= 0:
        return outerList
    for i in range(n):
        # create inner list
        innerList = []
        # Populate inner List
        if i == 0:
            innerList.append(1)
        elif i == 1:
            innerList.append(1)
            innerList.append(1)
        else:
            for a in range(i + 1):
                if a == 0 or a == i:
                    innerList.append(1)
                else:
                    tri = outerList[i - 1][a - 1] + outerList[i - 1][a]
                    innerList.append(tri)
        # popupulate outer list
        outerList.append(innerList)
    # Return outer list
    return outerList
