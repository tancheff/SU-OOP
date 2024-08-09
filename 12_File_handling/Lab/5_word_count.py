import os
import re

input_file = "5_input.txt"
words_file = "5_words.txt"
output_file = "5_output.txt"

sub_dir = "text_files"
root_dir = os.path.dirname(__file__)
print(root_dir)

input_file_path = os.path.join(root_dir, sub_dir, input_file)
words_file_path = os.path.join(root_dir, sub_dir, words_file)
output_file_path = os.path.join(root_dir, sub_dir, output_file)

with open(input_file_path, 'r') as file:
    input_words_no_edit = file.read()
    input_words = re.findall(r'\b[a-zA-Z]+\b', input_words_no_edit)

with open(words_file_path, 'r') as file:
    words = file.read().split(" ")

print(input_words)
print(words)

word_repetitions = {}

for word in input_words:
    lower_word = word.lower()
    if lower_word in words:

        if lower_word in word_repetitions:
            word_repetitions[lower_word] += 1
        else:
            word_repetitions[lower_word] = 1

print(word_repetitions)

sorted_word_repetitions = sorted(word_repetitions.items(), key=lambda kvp: -kvp[1])
print(sorted_word_repetitions)

with open(output_file_path, 'w') as file:
    for word, value in sorted_word_repetitions:
        file.write(f"{word} - {value}\n")
