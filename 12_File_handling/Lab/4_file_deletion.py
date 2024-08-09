import os.path

file_name = "3_my_first_file.txt"
sub_dir = "text_files"
root_dir = os.path.dirname(__file__)

file_path = os.path.join(root_dir, sub_dir, file_name)

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file has been removed: {file_path}")
else:
    print("File not found")

