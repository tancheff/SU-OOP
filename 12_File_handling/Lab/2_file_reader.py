import os.path

file_name = "2_numbers.txt"
sub_dir_name = "text_files"
root_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(root_dir, sub_dir_name, file_name)
print(file_path)

with open(file_path, "r") as file:
    data = file.readlines()

print(type(data))
print(data)
print(sum([int(num) for num in data]))
