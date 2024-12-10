#!python3

import numpy as np


def return_antinodes(a_x, a_y, b_x, b_y, max_dim):
    # returning values for part 1 solution
    result = []

    n1_x = 2 * a_x - b_x
    n1_y = 2 * a_y - b_y
    n2_x = 2 * b_x - a_x
    n2_y = 2 * b_y - a_y

    if n1_x in range(max_dim) and n1_y in range(max_dim):
        result.append([n1_x, n1_y])

    if n2_x in range(max_dim) and n2_y in range(max_dim):
        result.append([n2_x, n2_y])

    return result


def return_more_antinodes(a_x, a_y, b_x, b_y, max_dim):
    # returning values for part 2 solution
    result = []

    in_positive = True
    in_negative = True

    step_pos = 0
    step_neg = 0

    dx = b_x - a_x
    dy = b_y - a_y

    while in_positive:
        n1_x = b_x + step_pos * dx
        n1_y = b_y + step_pos * dy

        if n1_x in range(max_dim) and n1_y in range(max_dim):
            result.append([n1_x, n1_y])
            step_pos += 1
        else:
            in_positive = False

    while in_negative:
        n1_x = a_x - step_neg * dx
        n1_y = a_y - step_neg * dy

        if n1_x in range(max_dim) and n1_y in range(max_dim):
            result.append([n1_x, n1_y])
            step_neg += 1
        else:
            in_negative = False

    return result


if __name__ == '__main__':
    with open('data', 'r') as file:
        data = file.readlines()
        data = [list(_.strip()) for _ in data]
        np_data = np.array(data)

        length = 50

        antinodes = set()
        total = 0

        for i in range(length):
            for j in range(length):
                if data[i][j] == '.':
                    pass
                else:
                    frequency = data[i][j]
                    frequencies = np.argwhere(np_data == frequency)
                    for node in frequencies:
                        if node[0] == i and node[1] == j:
                            pass
                        else:
                            antinodes_frequency = return_more_antinodes(i, j, node[0], node[1], length)
                            for point in antinodes_frequency:
                                antinodes.add(f'{point[0]} {point[1]}')
                                total += 1

        print(len(antinodes))


