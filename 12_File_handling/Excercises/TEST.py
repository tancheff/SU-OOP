import os.path
from datetime import datetime


def create_and_rename_file():
    file_name = "0_text.txt"
    sub_dir = "text_files"
    root_dir = os.path.dirname(__file__)

    file_dir = os.path.join(root_dir, sub_dir, file_name)

    new_file_name = "01_text.txt"
    new_file_dir = os.path.join(root_dir, sub_dir, new_file_name)

    print(file_dir)
    print(new_file_dir)

    if os.path.isfile(file_dir):
        os.rename(file_dir, new_file_dir)
    else:
        os.rename(new_file_dir, file_dir)

    return file_dir


def experiment_with_files(file_dir: str):
    with open(file_dir, "w") as file:
        file.write("working with files is cool")

    with open(file_dir, "a") as file:
        file.write("\ntesting")

    with open(file_dir, "r") as file:
        print(file.readlines())

    file_info = os.stat(file_dir)
    print(file_info)
    print(f"file size: {file_info.st_size} bytes")
    print(f"last modified: {datetime.fromtimestamp(int(file_info.st_mtime))} sec")


file_dir = create_and_rename_file()

# print(experiment_with_files(file_dir))