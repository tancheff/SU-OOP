import os
from typing import LiteralString


def create_file(file_name: str) -> str:
    file_path = __get_file_path(file_name)
    already_created = __check_if_file_exists(file_name)

    with open(file_path, "w") as file:
        pass

    if already_created:
        return f"File {file_name} already exists. Its content has been cleared."
    else:
        return f"File {file_name} has been created."


def add_content(file_name: str, content: str) -> str:
    file_path = __get_file_path(file_name)

    # if not __check_if_file_exists(file_name):
    #     create_file(file_name)

    with open(file_path, 'a') as file:
        file.writelines(content + "\n")

    return f"{content} has been added to {file_name} file."


def replace_content(file_name: str, old_string: str, new_string: str) -> str:
    file_path = __get_file_path(file_name)

    if not __check_if_file_exists(file_name):
        return "An error occurred. File does not exist."

    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:

        for line in lines:
            file.write(line.replace(old_string, new_string))

        return f"<{old_string}> has been replaced with <{new_string}> "


def delete_file(file_name: str) -> str:
    file_path = __get_file_path(file_name)

    if not __check_if_file_exists(file_name):
        return "An error occurred. File does not exist."

    os.remove(file_path)
    return f"{file_name} has been successfully removed."


# HELPER METHODS
def __get_file_path(file_name) -> LiteralString | str | bytes:
    sub_dir = "text_files"
    root_dir = os.path.dirname(__file__)
    file_path = os.path.join(root_dir, sub_dir, file_name)

    return file_path


def __check_if_file_exists(file_name: str) -> bool:
    file_path = __get_file_path(file_name)

    return os.path.isfile(file_path)


user_inputs = [
    "Create-3_file.txt",
    "Add-3_file.txt-First Line",
    "Add-3_file.txt-Second Line",
    "Replace-3_random.txt-Some-some",
    "Replace-3_file.txt-First-1st",
    "Replace-3_file.txt-Second-2nd",
    "Delete-3_random.txt",
    "Delete-3_file.txt",
    "End"
]

functions = {
    "create": create_file,
    "add": add_content,
    "replace": replace_content,
    "delete": delete_file
}

while True:
    for user_input in user_inputs:
        if user_input == "End":
            break

        user_function, file_name, *content = user_input.split("-")

        user_function = user_function.lower()

        if user_function == "create":
            print(functions[user_function](file_name))
        elif user_function == "add":
            print(functions[user_function](file_name, content[0]))
        elif user_function == "replace":
            print(functions[user_function](file_name, content[0], content[1]))
        elif user_function == "delete":
            print(functions[user_function](file_name))
        else:
            print("Invalid command")

