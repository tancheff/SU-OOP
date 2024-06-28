def reverse_text(string: str):
    current_idx = len(string)-1
    while current_idx >= 0:
        yield string[current_idx]
        current_idx -= 1





for char in reverse_text("step"):
    print(char, end='')
