import os

file_name = "1_text.txt"
sub_dir_name = "text_files"
root_dir = os.path.dirname(os.path.abspath(__file__))


file_path = os.path.join(root_dir, sub_dir_name, file_name)
print(file_path)

try:
    data = open(file_path, "r").readlines()
    print(type(data))
    print(f"File found. Reading content:\n"
          f"{''.join(data)}")
except FileNotFoundError:
    print("File not found.")

# if-else variant:
# if os.path.isfile(file_path):
#     print("File found.")
# else:
#     print("File not found.")

