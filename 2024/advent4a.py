#!python3

import numpy as np

if __name__ == '__main__':
    with open('data', 'r') as file:
        data = file.readlines()
        data = [_.strip() for _ in data]

        total = 0

        for line in data:
            total += line.count('XMAS')
            total += line.count('SAMX')

        data_rotate = [[data[j][i] for j in range(len(data))] for i in range(len(data[0])-1,-1,-1)]

        data_rotate = [''.join(_) for _ in data_rotate]

        for line in data_rotate:
            total += line.count('XMAS')
            total += line.count('SAMX')

        # down slope
        for i in range(len(data)):
            data[i] = [_ for _ in data[i]]

        array = np.array(data)

        for i in range(-138, 137):
            line = array.diagonal(i)
            line = ''.join(line)
            total += line.count('XMAS')
            total += line.count('SAMX')

        # up slope
        for i in range(len(data_rotate)):
            data_rotate[i] = [_ for _ in data_rotate[i]]

        array = np.array(data_rotate)

        for i in range(-138, 137):
            line = array.diagonal(i)
            line = ''.join(line)
            total += line.count('XMAS')
            total += line.count('SAMX')
        print(total)
