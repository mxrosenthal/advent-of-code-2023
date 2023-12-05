from helper_methods import get_lines_from_file
from constants.constants_01 import digits_and_string_numbers, string_to_num_dict, digits_only


def get_number(line, reversed=False):
    if reversed:
        line = line[::-1]

    for item in line:
        if item in digits_only:
            return item

def solve_day_01_problem_1():
    lines = get_lines_from_file("data/data_01")
    total_sum = 0
    for line in lines:
        first = get_number(line)
        last = get_number(line, reversed=True)
        total_sum += (int(first) * 10) + int(last)

    print("day 1, problem 1 solution: ", total_sum)
    return total_sum

def solve_day_01_problem_2():
    lines = get_lines_from_file("data/data_01")

    total_sum = 0

    for line in lines:
        valid_lowest_digits = {}
        valid_highest_digits = {}

        for string in digits_and_string_numbers:
            lowest_index = line.find(string)
            highest_index = line.rfind(string)
            if lowest_index != -1: # ignore numbers not present in string
                valid_lowest_digits[string] = lowest_index

            if highest_index != -1:
                valid_highest_digits[string] = highest_index

        # gets the number with the starting index in the lowest spot
        first_num = min(valid_lowest_digits, key=valid_lowest_digits.get)
        # gets the number with the starting index in the highest spot
        last_num = max(valid_highest_digits, key=valid_highest_digits.get)

        num = string_to_num_dict.get(first_num) * 10 + string_to_num_dict.get(last_num)
        total_sum += num

    print("day 1, problem 2 solution: ", total_sum)
    return total_sum
