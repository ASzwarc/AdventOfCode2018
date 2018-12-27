from typing import List

def data_reader():
    data_input = []
    with open("Day3.txt") as f:
        for line in f:
            data_input.append(line)
    return data_input

def solver(input_list: List[str]):

    def get_params(input_string: str):
        at_pos = input_string.find("@")
        comma_pos = input_string.find(",")
        colon_pos = input_string.find(":")
        x_pos  =input_string.find("x")
        id = input_string[:at_pos-1]
        col = int(input_string[at_pos + 2: comma_pos])
        row = int(input_string[comma_pos + 1: colon_pos])
        width = int(input_string[colon_pos + 2: x_pos])
        height = int(input_string[x_pos+1:])
        return id, col, row, width, height

    size = 1010
    ids = set()
    fabric = [[(0, "#") for col in range(size)] for row in range(size)]
    for elem in input_list:
        id, col, row, width, height = get_params(elem)
        overlapped = False
        for y in range(row, row + height):
            for x in range(col, col + width):
                if fabric[y][x][0] > 0:
                    overlapped = True
                    if fabric[y][x][1] in ids:
                        ids.remove(fabric[y][x][1])
                fabric[y][x] = (fabric[y][x][0] + 1, id)
        if not overlapped:
            ids.add(id)
    sum = 0
    for row in range(size):
        for col in range(size):
            if fabric[row][col][0] > 1:
                sum += 1
    print("Sum: {}".format(sum))
    print("Non-overlapping id: {}".format(ids.pop()))

if __name__ == '__main__':
    input_list = data_reader()
    solver(input_list)