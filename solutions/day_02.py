from helper_methods import get_lines_from_file

red_limit = 12
green_limit = 13
blue_limit = 14

def get_game_number(line):
    return int(line.split(":")[0].split(" ")[1])

def get_sets_per_game(line):
    return line.split(":")[1].strip().split(";")

def get_num_for_color(current_set, color):
    pieces = current_set.split(", ")
    for piece in pieces:
        if piece.find(color) != -1:
            return int(piece.strip().split(" ")[0])
    return 0

def is_game_valid(sets_per_game):
    for current_set in sets_per_game:
        # current_set = '1 red, 5 blue, 1 green'
        num_red, num_green, num_blue = get_rgb_tuple(current_set)
        if set_is_invalid(num_red, num_green, num_blue):
            return False
    return True

def get_rgb_tuple(current_set):
    num_red = get_num_for_color(current_set, "red")
    num_green = get_num_for_color(current_set, "green")
    num_blue = get_num_for_color(current_set, "blue")
    return num_red, num_green, num_blue

def set_is_invalid(red, green, blue):
    if red > red_limit:
        return True
    if green > green_limit:
        return True
    if blue > blue_limit:
        return True
    return False

def solve_day_02_problem_1():
    lines = get_lines_from_file("data/data_02")
    total_sum = 0
    for line in lines:
        game_number = get_game_number(line)
        sets_per_game = get_sets_per_game(line)
        if is_game_valid(sets_per_game):
            total_sum += game_number

    print("day 2, problem 1 solution: ", total_sum)
    return total_sum

def solve_day_02_problem_2():
    lines = get_lines_from_file("data/data_02")
    # for each game 1-100 we want to find the highest num for each color.
    # once we have the highest num for each color we want to multiply the 3 nums together to get the power for that game.
    # sum the power of each game to get the solution

    total_sum = 0
    for line in lines:
        sets_per_game = get_sets_per_game(line)
        highest_red = 0
        highest_green = 0
        highest_blue = 0
        for current_set in sets_per_game:
            red, green, blue = get_rgb_tuple(current_set)
            if red > highest_red:
                highest_red = red
            if green > highest_green:
                highest_green = green
            if blue > highest_blue:
                highest_blue = blue

        power = highest_red * highest_green * highest_blue
        total_sum += power

    print("day 2, problem 2 solution: ", total_sum)
    return total_sum