import os

def get_lines_from_file(file_path):
    root_directory = os.path.join(os.path.dirname(__file__), "")
    data_path = os.path.join(root_directory, file_path)

    f = open(data_path, "r")
    lines = f.readlines()
    lines = [line[:-1] for line in lines]
    return lines