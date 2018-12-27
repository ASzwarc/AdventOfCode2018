import re
import operator
def input_reader():
    input_list = []
    with open("Day4.txt") as f:
        for line in f:
            input_list.append(line)
    return input_list

def solver1(input_list):
    input_sorted = sorted(input_list)
    id_sleep_dict = {}
    for line in input_sorted:
        time = int(re.search(r'\[(.* \d{2}:)(\d{2})\]', line).group(2))
        if line.find("Guard") != -1:
            id = re.search(r'#(\d+)', line).group(1)
            id_sleep_dict.setdefault(id, [0 for i in range(60)])
        elif line.find("falls") != -1:
            start = time
        elif line.find("wakes") != -1:
            for i in range(start, time):
                id_sleep_dict[id][i] += 1
    max_sleeping_sum = 0
    max_sleeping_id = ""
    max_sleeping_minute = -1
    max_sleeping_freq = -1
    max_freq_sleeper_id = ""
    for key, value in id_sleep_dict.items():
        # part 2 of challenge
        sleeping_minute, sleeping_freq = max(enumerate(id_sleep_dict[key]), key=operator.itemgetter(1))
        if sleeping_freq > max_sleeping_freq:
            max_sleeping_freq = sleeping_freq
            max_sleeping_minute = sleeping_minute
            max_freq_sleeper_id = key
        # part 1 of challenge
        sleeping_sum = sum(value)
        if sleeping_sum > max_sleeping_sum:
            max_sleeping_sum = sleeping_sum
            max_sleeping_id = key
    max_index, max_value = max(enumerate(id_sleep_dict[max_sleeping_id]), key=operator.itemgetter(1))
    print("{}: {} -> {}".format(max_sleeping_id, max_index, max_value))
    print("{}: {} -> {}".format(max_freq_sleeper_id, max_sleeping_minute, max_sleeping_freq))

if __name__ == '__main__':
    data = input_reader()
    solver1(data)