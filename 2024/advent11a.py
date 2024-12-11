#!python3

if __name__ == '__main__':
    with open('data_test', 'r') as file:
        data = file.readlines()
        data = data[0]
        stones = data.split(' ')
        stones = [int(_) for _ in stones]

        for i in range(25):
            new_stones = []
            for stone in stones:
                _ = len(str(stone))
                _1 = len(str(stone)) % 2
                if stone == 0:
                    new_stones.append(1)
                elif len(str(stone)) % 2 == 0:
                    stone_string = str(stone)
                    length = len(stone_string)
                    cutoff = int(length / 2)
                    first = int(stone_string[:cutoff])
                    second = int(stone_string[cutoff:])
                    new_stones.append(int(first))
                    new_stones.append(int(second))
                else:
                    new_stones.append(2024 * stone)

            stones = new_stones

        print(len(stones))