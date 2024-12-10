#!python3


def compute_total(numbers, operator_list, target):
    total = numbers[0]
    if total == target:
        return 1

    for i in range(len(operator_list)):
        if operator_list[i] == '+':
            total += numbers[i+1]
        else:
            total *= numbers[i+1]

        if total == target:
            return 1
        elif total > target:
            return -2

    return -1


def create_operator_list(length, number):
    operators = []
    for i in range(length):
        operators.append('+')

    format_list = str(0)
    format_list += str(length)
    format_list += 'b'
    binary_list = format(number, format_list)

    for i in range(length):
        if binary_list[i] == '1':
            operators[i] = '*'

    return operators


if __name__ == '__main__':
    with open('data', 'r') as file:
        data = file.readlines()
        data = [_.strip() for _ in data]

        correct = 0

        for line in data:
            data_list = line.split(' ')
            result = int(data_list[0][:-1])
            values = data_list[1:]
            values = [int(_) for _ in values]

            steps = pow(2, len(values))

            works = False
            for iteration in range(steps):
                new_operators = create_operator_list(len(values) - 1, iteration)
                return_val = compute_total(values, new_operators, result)
                if return_val == 1:
                    works = True

            if works:
                print(result)
                correct += result

        print(correct)





