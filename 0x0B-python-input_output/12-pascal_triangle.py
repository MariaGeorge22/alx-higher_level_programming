#!/usr/bin/python3
"""
10th Task
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    pascal_triangle_list = []
    for i in range(n):
        if i == 0:
            pascal_triangle_list.append([1])
        elif i == 1:
            pascal_triangle_list.append([1, 1])
        else:
            inner_list = []
            for j in range(i+1):
                if j == 0 or j == i:
                    inner_list.append(1)
                else:
                    old_list = pascal_triangle_list[i-1]
                    inner_list.append(old_list[j-1]+old_list[j])
            pascal_triangle_list.append(inner_list)
    return pascal_triangle_list
