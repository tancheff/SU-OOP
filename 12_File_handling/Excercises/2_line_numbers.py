import os.path
import re

text_file = "2_text.txt"
text_result = "2_text_result.txt"
sub_dir = "text_files"
root_dir = os.path.dirname(__file__)
text_file_path = os.path.join(root_dir, sub_dir, text_file)
text_result_path = os.path.join(root_dir, sub_dir, text_result)

letters = r'[a-zA-Z]'
punctuation = r'[^\w\s]'

with open(text_file_path, "r") as file:
    text = file.readlines()

result = []

for i in range(0, len(text)):
    letters_count = len(re.findall(letters, text[i]))
    punctuation_count = len(re.findall(punctuation, text[i]))

    result.append(f"Line {i+1}: {text[i].replace('\n', "")} ({letters_count})({punctuation_count})\n")

with open(text_result_path, "w") as file:
    for line in result:
        file.write(line)
