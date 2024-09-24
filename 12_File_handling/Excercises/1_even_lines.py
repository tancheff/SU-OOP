import os
import re

file_name = "1_text.txt"
sub_dir = "text_files"
root_dir = os.path.dirname(__file__)

file_path = os.path.join(root_dir, sub_dir, file_name)
print(file_path)

symbols = ["-", ",", ".", "!", "?"]

with open(file_path, "r") as file:
    lines = file.readlines()
    print(lines)

for row in range(0, len(lines), 2):
    for symbol in symbols:
        lines[row] = lines[row].replace(symbol, "@")

    print(lines[row], end="")


