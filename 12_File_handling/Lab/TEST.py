import os
import datetime

absolute_script_path = os.path.abspath(__file__)
print(absolute_script_path)  # C:\Users\a1bg537570\PycharmProjects\OOP\SU-OOP\12_File_handling\Lab\TEST.py

absolute_path = os.path.abspath(".")

print(absolute_path)  # C:\Users\a1bg537570\PycharmProjects\OOP\SU-OOP\12_File_handling\Lab
print(type(absolute_path))  # <class 'str'>

# the right way to get the working directory is:
absolute_path_dir_name = os.path.dirname(os.path.abspath(__file__))
print(absolute_path_dir_name)
# exit()

file_name = "text_files/1_text.txt"
sub_dir_name = "text_files"

file_path = os.path.join(absolute_path_dir_name, sub_dir_name, file_name)
print(os.path.isfile(file_path))

print(file_path)  # C:\Users\a1bg537570\PycharmProjects\OOP\SU-OOP\12_File_handling\Lab\text_files\1_text.txt
print()

path = "C:\\Users\\a1bg537570\\Desktop"

file = open(file_path, "r")
lines = file.readlines()

print(type(lines))
print(lines)
print()

for index in range(len(lines)):
    cleared_text = lines[index].replace("\n", "")
    print(f"Row {index + 1} cointains: {cleared_text}")

file.close()

print()

file = open(file_path)

# Experimenting with the try-catch block:
try:
    nums = [int(el) for el in file.readlines()]
    # add some logic here
except ValueError:
    print("You're doing something that's not right man...")
finally:  # това винаги се изпълнява
    file.close()
    print("File is now closed.")

print("\n")

# How to rename a file:
current_date = datetime.datetime.now()
date_str = current_date.strftime("%Y-%m-%d")
sub_dir_path = os.path.join(absolute_path_dir_name, sub_dir_name)
new_name = os.path.join(sub_dir_path, f"{date_str}_{file_name}")

os.rename(file_path, new_name)
print(f"File successfully renamed:\n"
      f"From:   {file_path}\n"
      f"To:     {new_name}")

"""VIDEO PROGRESS 1:17:49"""
