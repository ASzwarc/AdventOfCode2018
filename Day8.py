from typing import List

def data_reader() -> List[int]:
    with open("Day8.txt") as f:
        return list(map(int, f.readline().split(" ")))

def solver(input_list: List[int]) -> None:
    child_no, metadata_size = input_list[:2]
    input_list = input_list[2:]
    metadata_sum = 0
    metadata = []
    child_vals = []
    total = 0

    for _ in range(child_no):
        input_list, child_sum, _, total = solver(input_list)
        metadata_sum += child_sum
        child_vals.append(total)

    metadata = input_list[:metadata_size]
    metadata_sum += sum(metadata)
    input_list = input_list[metadata_size:]

    if child_no > 0:
        total = sum([child_vals[x-1] for x in metadata if len(child_vals) > 0 and x <= len(child_vals)])
    else:
        total = metadata_sum
    return input_list, metadata_sum, metadata, total




if __name__ == '__main__':
    input_list = [3, 4, 1, 3, 0, 2, 0, 0, 10, 11, 12, 1, 1, 0, 1, 99, 1, 0, 2, 1, 1, 1, 1, 2, 3]
    #print(solver(input_list)[1])
    #print(solver(input_list)[3])
    #print(solver(data_reader())[1])
    print(solver(data_reader())[3])