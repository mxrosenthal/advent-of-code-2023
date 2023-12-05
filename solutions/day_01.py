import json
import ast


def get_first_number(line):
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    for item in line:
        if item in numbers:
            print(item)
            return item

def get_last_number(line):
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    reversed_line = line[::-1]

    for item in reversed_line:
        if item in numbers:
            print(item)
            return item

def do_the_thing_1():
    f = open("aoc_day_01_data.py","r")
    lines = f.readlines()
    lines = [line[:-1] for line in lines]
    sum = 0
    for line in lines[0:1]:
        print(type(line))
        print(line)
        first = get_first_number(line)
        print(first)
        last = get_last_number(line)
        num = ((int(first) * 10) + int(last))
        print(num)
        sum += num

    print(sum)

def do_the_thing_2():
    f = open("aoc_day_01_data.py","r")
    lines = f.readlines()
    lines = [line[:-1] for line in lines]
    sum = 0
    all_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0","1","2","3","4","5","6","7","8","9"]
    string_to_num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "0": 0,"1": 1,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9}
    for line in lines:
        # print(line)
        valid_lowest_digits = {}
        valid_highest_digits = {}

        for string in all_nums:
            lowest_index = line.find(string)
            highest_index = line.rfind(string)
            if lowest_index != -1:
                valid_lowest_digits[string] = lowest_index

            if highest_index != -1:
                valid_highest_digits[string] = highest_index

        first_num = min(valid_lowest_digits, key=valid_lowest_digits.get)
        last_num = max(valid_highest_digits, key=valid_highest_digits.get)
        # print(valid_lowest_digits)
        # print(valid_highest_digits)
        # print(first_num, string_to_num_dict.get(first_num))
        # print(last_num, string_to_num_dict.get(last_num))\
        num = string_to_num_dict.get(first_num) * 10 + string_to_num_dict.get(last_num)
        sum += num
    print(sum)

if __name__ == "__main__":
    # do_the_thing_1()
    do_the_thing_2()
