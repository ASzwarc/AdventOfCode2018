import re

def data_reader():
    output_list = []
    with open("Day6.txt") as f:
        for line in f:
            match = re.match(r'(\d+), (\d+)', line)
            col = match.group(1)
            row = match.group(2)
            output_list.append((int(col), int(row)))
    return output_list


def solver(input_list):
    result = {}
    infinite_ids = set()
    size = 410
    max_dist_to_coordinates = 10000
    total_size = 0
    #matrix = [[0 for col in range(size)] for row in range(size)]
    for row in range(size):
        for col in range(size):
            min_distance = size + 1
            point_id = 0
            same_distance = False
            dist_to_coordinate = 0
            for i, point in enumerate(input_list):
                manhattan_dist = abs(col - point[0]) + abs(row - point[1])
                dist_to_coordinate += manhattan_dist
                if manhattan_dist < min_distance:
                    same_distance = False
                    min_distance = manhattan_dist
                    point_id = i + 1
                elif min_distance == manhattan_dist:
                    same_distance = True
            if dist_to_coordinate < max_dist_to_coordinates:
                total_size += 1
            if not same_distance:
                #matrix[row][col] = point_id
                result.setdefault(point_id, 0)
                result[point_id] += 1
                if row == 0 or row == size - 1 or col == 0 or col == size - 1:
                    infinite_ids.add(point_id)
    for id in infinite_ids:
        del result[id]
    # print("\n".join(["".join(map(str, x)) for x in matrix]))
    print("Result {} {}".format(result, infinite_ids))
    print("Largest area {}".format(result.get(max(result.keys(), key = lambda k: result[k]))))
    print("Total distance {}".format(total_size))

if __name__ == '__main__':
    input_list = data_reader()
    #input_list = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
    solver(input_list)