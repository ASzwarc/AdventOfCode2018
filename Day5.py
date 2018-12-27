
def data_reader():
    with open("Day5.txt") as f:
        for line in f:
            return list(line)

def remove_pairs(input_list):
    i = 1
    while i < len(input_list):
        if abs(ord(input_list[i-1]) - ord(input_list[i])) == 32:
            del input_list[i - 1]
            del input_list[i - 1]
            #print(input_list)
            i -= 1
        else:
            i += 1
    return len(input_list)

def most_optimal_polymer(input_string):
    result = {}
    for asciiLetter in range(65, 91):
        big = asciiLetter
        small = asciiLetter + 32
        transformed = input_string.translate({big: None, small: None})
        result[chr(small) + chr(big)] = remove_pairs(list(transformed))
    return result.get(min(result.keys(), key = (lambda k: result[k])))

if __name__ == '__main__':
    #input_list = list("dabAcCaCBAcCcaDA")
    input_list = data_reader()
    #remove_pairs(input_list)
    print(most_optimal_polymer("".join(input_list)))