#!python3

from collections import defaultdict

if __name__ == '__main__':
    with open('data', 'r') as file:
        stones = [int(_) for _ in file.readlines()[0].split(' ')]

        dict_data = defaultdict(int)
        for stone in stones:
            dict_data[stone] += 1

        for _ in range(75):
            new_stones = defaultdict(int)
            for stone in dict_data:
                stone_string = str(stone)
                if stone == 0:
                    new_stones[1] += dict_data[0]
                elif len(str(stone)) % 2 == 0:
                    new_stones[int(stone_string[:(int(len(str(stone)) / 2))])] += dict_data[stone]
                    new_stones[int(stone_string[(int(len(str(stone)) / 2)):])] += dict_data[stone]
                else:
                    new_stones[stone * 2024] += dict_data[stone]
            dict_data = new_stones

        print(sum(dict_data[_] for _ in dict_data))