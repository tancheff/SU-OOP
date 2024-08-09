import os

new_file_name = "3_my_first_file.txt"
sub_dir = "text_files"
root_dir = os.path.dirname(os.path.abspath(__file__))

print(root_dir)

new_file_path = os.path.join(root_dir, sub_dir, new_file_name)
new_file_lines = "I just created my first file!"

with open(new_file_path, 'w') as file:
    file.write(new_file_lines)
    print("File creation successfull.")

with open(new_file_path, 'r') as file:
    data = file.readlines()
    print(data)
    