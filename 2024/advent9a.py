#!python3

if __name__ == '__main__':
    with open('data', 'r') as file:
        data = file.readlines()
        data = [list(_.strip()) for _ in data]
        data = data[0]

        disk_array = []

        on_gap = False
        id = 0

        for i in range(len(data)):
            if on_gap:
                disk_array.append([None, int(data[i])])
                on_gap = False
            else:
                disk_array.append([id, int(data[i])])
                id += 1
                on_gap = True

        checksum = 0
        idx = 0
        done = False
        final = []

        while not done:
            if len(disk_array) == 0:
                done = True
            else:
                current = disk_array.pop(0)
                if current[0] is not None:
                    final.append(current)
                    for i in range(current[1]):
                        checksum += idx * current[0]
                        idx += 1
                else:
                    # on a gap, will something fit here?
                    gap_size = current[1]
                    last = disk_array[-1] # last entry in the disk array table
                    if last[0] is None:
                        disk_array.pop()
                        last = disk_array[-1]
                    if gap_size > last[1]:
                        disk_array.insert(0, [None, gap_size - last[1]])
                        disk_array.insert(0, last)
                        disk_array.pop()
                    elif gap_size == last[1]:
                        disk_array.insert(0, last)
                        disk_array.pop()
                    else:
                        disk_array.insert(0, [last[0], gap_size])
                        disk_array.pop()
                        disk_array.append([last[0], last[1] - gap_size])

        print(checksum)


