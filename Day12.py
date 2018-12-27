import re

def solver(initial_state, rules_list):
    #return sum of indexes of pots with plants
    parsed_rules_list = []
    rule_pattern = re.compile(r'([#.]{5}) => ([#.])')
    for rule in rules_list:
        matched = re.match(rule_pattern, rule)
        parsed_rules_list.append(tuple(matched.groups()))
    state = "...." + initial_state + "...."
    print("0: {}".format(state))
    previous_state = 0
    for generation in range(1, 301): #20 generations starting from 1
        new_state = ["."] * len(state)
        for pot in range(2, len(state) - 2):
            for rule in parsed_rules_list:
                if state[pot - 2: pot + 3] == rule[0]:
                    # print("Rule {} matches {}. Pot {} changed to {}".format(rule[0], state[pot - 2: pot + 3], pot, rule[1]))
                    new_state[pot]= rule[1]
        state = "...." + "".join(new_state) + "...."
        # print("{}: {}".format(generation, state))
        zero_pot_index = (generation + 1) * 4
        # if generation == 20:
        #     print([i - zero_pot_index for i, elem in enumerate(state) if elem == "#"])
        result = sum([i - zero_pot_index for i, elem in enumerate(state) if elem == "#"])
        new_diff = result - previous_state
        #print("{} -> {}, diff = {}".format(generation, result, diff))
        previous_state = result
    print("Generation {} -> {}, diff = {}".format(generation, result, new_diff))
    final_generation = 50000000000
    final_result = result + (final_generation - generation) * new_diff
    print("Result for {} is {}".format(final_generation, final_result))

    

if __name__ == "__main__":
    initial_state  = "#....##.#.#.####..#.######..##.#.########..#...##...##...##.#.#...######.###....#...##..#.#....##.##"
    rules_list = [".#.## => #", 
                  ".#.#. => #", 
                  "#.#.# => .", 
                  ".#### => .", 
                  ".#... => .", 
                  "#..## => .", 
                  "..#.# => #", 
                  "#.#.. => .", 
                  "##### => .", 
                  "....# => .", 
                  "...## => .", 
                  "..##. => .", 
                  "##.#. => #", 
                  "##..# => .", 
                  "##... => #", 
                  "..### => #", 
                  ".##.. => #", 
                  "###.. => .", 
                  "#..#. => .", 
                  "##.## => .", 
                  "..#.. => #", 
                  ".##.# => #", 
                  "####. => #", 
                  "#.### => .", 
                  "#...# => #", 
                  "###.# => #", 
                  "...#. => #", 
                  ".###. => .", 
                  ".#..# => #", 
                  "..... => .", 
                  "#.... => .", 
                  "#.##. => #"]
    solver(initial_state, rules_list)