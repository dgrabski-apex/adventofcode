#!/bin/python3


def looped(loc_x, loc_y, direction, data_map, iteration):
    steps = 0
    while True:
        steps += 1

        if str(direction) in data_map[loc_y][loc_x]:
            return True
        else:
            if data_map[loc_y][loc_x] == '.' or \
                data_map[loc_y][loc_x] == '^' or \
                data_map[loc_y][loc_x] == '>' or \
                data_map[loc_y][loc_x] == 'v' or \
                    data_map[loc_y][loc_x] == '<':
                data_map[loc_y][loc_x] = str(direction)
            else:
                data_map[loc_y][loc_x] += str(direction)

            loc_x_next = loc_x + (1 if direction == 1 else 0) - (1 if direction == 3 else 0)
            loc_y_next = loc_y + (1 if direction == 2 else 0) - (1 if direction == 0 else 0)

            if (loc_y_next == 130) or (loc_x_next == 130) or (loc_y_next == -1) or (loc_x_next == -1):
                # exit!
                return False
            elif data_map[loc_y_next][loc_x_next] == '#':
                direction = (direction + 1) % 4
            else:
                loc_x = loc_x_next
                loc_y = loc_y_next


if __name__ == '__main__':
    with open('data', 'r') as file:
        data = file.readlines()
        place_map = [list(_.strip()) for _ in data]

        dimension = 130

        direction = None
        found_start = False
        loc_x = None
        loc_y = None

        i = 0
        for line in place_map:
            if '^' in line:
                direction = 0
                found_start = True
                loc_x = line.index('^')
            if '>' in line:
                direction = 1
                found_start = True
                loc_x = line.index('>')
            if 'v' in line:
                direction = 2
                found_start = True
                loc_x = line.index('v')
            if '<' in line:
                direction = 3
                found_start = True
                loc_x = line.index('<')

            if found_start:
                loc_y = i
                found_start = False
            i += 1

        """
        Got our starting location
        Next step:
            direction = 0: y--
            direction = 1: x++
            direction = 2: y++
            direction = 3: x--
        """
        obstructions = 0
        possibles = 0
        iteration = 0

        for obs_x in range(dimension):
            for obs_y in range(dimension):
                iteration += 1
                if place_map[obs_y][obs_x] == '.':
                    obs_place_map = []
                    for line in place_map:
                        obs_place_map.append(line.copy())
                    obs_place_map[obs_y][obs_x] = '#'
                    possibles += 1

                    if looped(loc_x, loc_y, direction, obs_place_map, iteration):
                        obstructions += 1

        print(obstructions)