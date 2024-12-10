#!python3


def locate(in_map, target_value, map_size):
    results = []

    for i in range(map_size):
        for j in range(map_size):
            if in_map[i][j] == target_value:
                results.append([i, j])
    return results


def find_next_step_rating(in_map, i_loc, j_loc, target_value, map_size):
    if target_value == 10:
        return 1

    results = []
    if i_loc+1 in range(map_size):
        if in_map[i_loc+1][j_loc] == target_value:
            results.append([i_loc+1, j_loc])
    if i_loc-1 in range(map_size):
        if in_map[i_loc-1][j_loc] == target_value:
            results.append([i_loc-1, j_loc])
    if j_loc+1 in range(map_size):
        if in_map[i_loc][j_loc+1] == target_value:
            results.append([i_loc, j_loc+1])
    if j_loc-1 in range(map_size):
        if in_map[i_loc][j_loc-1] == target_value:
            results.append([i_loc, j_loc-1])

    total = 0
    for result in results:
        total += find_next_step_rating(in_map, result[0], result[1], target_value+1, map_size)
    return total


def find_next_step_score(in_map, i_loc, j_loc, target_value, map_size):
    if target_value == 10:
        return {f'{i_loc},{j_loc}'}

    results = []
    if i_loc+1 in range(map_size):
        if in_map[i_loc+1][j_loc] == target_value:
            results.append([i_loc+1, j_loc])
    if i_loc-1 in range(map_size):
        if in_map[i_loc-1][j_loc] == target_value:
            results.append([i_loc-1, j_loc])
    if j_loc+1 in range(map_size):
        if in_map[i_loc][j_loc+1] == target_value:
            results.append([i_loc, j_loc+1])
    if j_loc-1 in range(map_size):
        if in_map[i_loc][j_loc-1] == target_value:
            results.append([i_loc, j_loc-1])

    result_set = set()
    for result in results:
        new_set_entries = find_next_step_score(in_map, result[0], result[1], target_value+1, map_size)
        for new_entry in new_set_entries:
            result_set.add(new_entry)

    return result_set


if __name__ == '__main__':
    with open('data', 'r') as file:
        data = file.readlines()
        data = [list(_.strip()) for _ in data]

        map = []
        for line in data:
            characters = list(line)
            map.append([int(_) for _ in characters])

        size = len(map[0])

        trailheads = locate(map, 0, size)

        part_a_list = set()
        for trailhead in trailheads:
            new_set_values = find_next_step_score(map, trailhead[0], trailhead[1], 1, size)
            for value in new_set_values:
                part_a_list.add(value)
        part_a_score = len(part_a_list)

        part_b_score = 0
        for trailhead in trailheads:
            part_b_score += find_next_step_rating(map, trailhead[0], trailhead[1], 1, size)

        print(f'Part 1: {part_a_score}')
        print(f'Part 2: {part_b_score}')