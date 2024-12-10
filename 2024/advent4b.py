#!python3


def check(i, j, data):
    works = False
    if data[i][j] == 'A':
        a = data[i-1][j+1]
        b = data[i-1][j-1]
        c = data[i+1][j+1]
        d = data[i+1][j-1]
        result = a + b + c + d

        if result.count('M') == 2:
            if result.count('S') == 2:
                if b != c:
                    works = True

    return works


if __name__ == '__main__':
    with open('data', 'r') as file:
        data = file.readlines()
        data = [_.strip() for _ in data]
        for i in range(len(data)):
            data[i] = [_ for _ in data[i]]

        total = 0

        for i in range(1,139):
            for j in range(1,139):
                if check(i, j, data):
                    total += 1

        print(total)