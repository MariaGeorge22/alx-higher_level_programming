#!/usr/bin/python3
"""
Optional Task 1
"""
import sys


def nqueens(size=""):
    """
    solves the nqueens problem
    """
    if not size.isdigit():
        print("N must be a number")
        sys.exit(1)
    int_size = int(size)
    if int_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    all_positions = get_all_positions(int_size)
    possible_solutions = get_possible_solutions(all_positions)
    for solution in possible_solutions:
        print(solution)


def get_all_positions(size=0):
    """
    returns list of all positions
    """
    positions = []
    for i in range(size):
        for j in range(size):
            positions.append([i, j])
    return positions


def get_possible_solutions(positions=[]):
    """
    returns list of possible solutions
    """
    solutions = []
    first = list(positions)
    second = list(positions)
    third = list(positions)
    fourth = list(positions)
    for first_position in first:
        for second_position in second:
            for third_position in third:
                for fourth_position in fourth:
                    if check_if_valid_solution(
                        first_position,
                        second_position,
                        third_position,
                        fourth_position,
                    ):
                        solutions.append([first_position,
                                          second_position,
                                          third_position,
                                          fourth_position,])
                        for current_list in [first, second, third, fourth]:
                            if first_position in current_list:
                                current_list.remove(first_position)
                            if second_position in current_list:
                                current_list.remove(second_position)
                            if third_position in current_list:
                                current_list.remove(third_position)
                            if fourth_position in current_list:
                                current_list.remove(fourth_position)
    return solutions


def check_if_valid_solution(
    pos_1=[],
    pos_2=[],
    pos_3=[],
    pos_4=[],
):
    """
    check if solution is valid
    """
    # print(
    #     f"current position possibilites: pos_1:{pos_1}\npos_2:{pos_2}\npos_3:{pos_3}\npos_4{pos_4}")
    if pos_1[0] == pos_2[0]\
            or pos_1[1] == pos_2[1]\
            or pos_1[0]**2+pos_1[1]**2 == pos_2[0]**2+pos_2[1]**2:
        return False
    if pos_1[0] == pos_3[0]\
            or pos_1[1] == pos_3[1]\
            or pos_1[0]**2+pos_1[1]**2 == pos_3[0]**2+pos_3[1]**2:
        return False
    if pos_1[0] == pos_4[0]\
            or pos_1[1] == pos_4[1]\
            or pos_1[0]**2+pos_1[1]**2 == pos_4[0]**2+pos_4[1]**2:
        return False
    if pos_2[0] == pos_3[0]\
            or pos_2[1] == pos_3[1]\
            or pos_2[0]**2+pos_2[1]**2 == pos_3[0]**2+pos_3[1]**2:
        return False
    if pos_2[0] == pos_4[0]\
            or pos_2[1] == pos_4[1]\
            or pos_2[0]**2+pos_2[1]**2 == pos_4[0]**2+pos_4[1]**2:
        return False
    if pos_3[0] == pos_4[0]\
            or pos_3[1] == pos_4[1]\
            or pos_3[0]**2+pos_3[1]**2 == pos_4[0]**2+pos_4[1]**2:
        return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
