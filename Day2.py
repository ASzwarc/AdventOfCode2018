import unittest
from collections import Counter
from typing import List
from difflib import SequenceMatcher

def data_runner(func):
    input_list = []
    with open("Day2.txt") as f:
        for line in f:
            input_list.append(line)
    print(func(input_list))

def solver(input_list: List[str]) -> int:
    two_count = 0
    three_count = 0
    for elem in input_list:
        is_two = False
        is_three = False
        counter = Counter(elem)
        for _, value in counter.items():
            if value == 2 and not is_two:
                two_count += 1
                is_two = True
            elif value == 3 and not is_three:
                three_count += 1
                is_three = True
    return two_count * three_count

def solver2(input_list: List[str]) -> int:
    
    def compare_half(hash_table, word_range):
        for _, val_list in hash_table.items():
            if len(val_list) > 1:
                for index, element in enumerate(val_list):
                    for index_rest, element_rest in enumerate(val_list):
                        count_diff = 0
                        if index != index_rest:
                            for i in range(word_range[0], word_range[1]):
                                if element[i] != element_rest[i]:
                                    count_diff += 1
                        if count_diff == 1:
                            return True, element, element_rest
        return False, str(), str()

    hashing_table_first = dict()
    hashing_table_second = dict()
    hash_size = int(len(input_list[0]) / 2 + 1)
    for elem in input_list:
        elem_first = elem[ : hash_size]
        elem_second = elem[hash_size : ]
        key_first = hash(elem_first)
        key_second = hash(elem_second)
        hashing_table_first.setdefault(key_first, [])
        hashing_table_second.setdefault(key_second, [])
        hashing_table_first[key_first].append(elem)
        hashing_table_second[key_second].append(elem)
    result, word1, word2 = compare_half(hashing_table_first, (hash_size, len(input_list[0])))
    if not result:
        _, word1, word2 = compare_half(hashing_table_second, (0, hash_size))
    
    match = SequenceMatcher(None, word1, word2).find_longest_match(0, len(word1), 0, len(word2))
    print(word1[match.a:match.a + match.size] + word1[match.size + 1:])

class SolutionTests(unittest.TestCase):

    def test_first(self):
        input_list = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
        self.assertEqual(solver(input_list), 12)
    
    def test_second(self):
        input_list = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
        self.assertEqual(solver2(input_list), "fgij")


if __name__ == '__main__':
    data_runner(solver2)