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

        for i in range(id-1, -1, -1):
            found = False # found the block of data where i is the correct id
            idx = -1
            while not found:
                search_point = disk_array[idx]

                if search_point[0] is None and idx == -1:
                    disk_array.pop()
                elif search_point[0] == i:
                    found = True
                else:
                    idx -= 1

            found_home = False  # have we found a new home for that block of data?
            block_idx = 0
            block_needed = search_point[1]  # needed blank block size
            block_id = search_point[0]  # which also equals i, oh well

            j = 0
            while j < (len(disk_array) + idx) and not found_home:
                if disk_array[j][0] is None:
                    block_available = disk_array[j][1]
                    if block_available == block_needed:
                        disk_array[j][0] = block_id
                        disk_array[idx][0] = None
                        found_home = True
                    elif block_available < block_needed:
                        pass
                    elif block_available > block_needed:
                        disk_array[j][0] = block_id
                        total_space = block_available
                        disk_array[j][1] = block_needed
                        disk_array.insert(j+1, [None, total_space - block_needed])
                        disk_array[idx][0] = None
                        found_home = True
                j += 1

        checksum = 0
        out_idx = 0
        for block in disk_array:
            block_id = block[0]
            block_length = block[1]
            if block_id is None:
                out_idx += block_length
            else:
                for i in range(block_length):
                    checksum += int(block_id) * out_idx
                    out_idx += 1

        print(checksum)
