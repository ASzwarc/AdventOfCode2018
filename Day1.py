import unittest
from typing import List

def solution():
    sum = 0
    with open("Day1.txt") as f:
        for line in f:
            sum += int(line)
    print("Solution: {}".format(sum))

def solution2():
    inputList = []
    with open("Day1.txt") as f:
        for line in f:
            inputList.append(int(line))
    print("Solution2: {}".format(solver(inputList)))

def solver(input_list: List[int]) -> int:
    current_freq = 0
    freq_set = {current_freq}
    while True:
        for elem in input_list:
            current_freq += elem
            if current_freq in freq_set:
                return current_freq
            else:
                freq_set.add(current_freq)

class SolutionTests(unittest.TestCase):
    
    def test_first(self):
        intput_list = [1, -1]
        self.assertEqual(solver(intput_list), 0)

    def test_second(self):
        intput_list = [3, 3, 4, -2, -4]
        self.assertEqual(solver(intput_list), 10)

    def test_third(self):
        intput_list = [-6, 3, 8, 5, -6]
        self.assertEqual(solver(intput_list), 5)

    def test_fourth(self):
        intput_list = [7, 7, -2, -7, -4]
        self.assertEqual(solver(intput_list), 14)

if __name__ == '__main__':
    solution2()
    unittest.main()