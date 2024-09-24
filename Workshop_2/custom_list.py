from typing import List


class CustomList:
    def __init__(self, *nums):
        self.__list = list(nums)

    def append(self, value):
        self.__list.append(value)
        return self.__list

    def remove(self, index: int):
        removed_val = self.__list[index]
        self.__list.remove(removed_val)
        return removed_val

    def get_index(self, index: int):
        return self.__list[index]

    def extend(self, value: List[int or str]):
        self.__list = [num for num in self.__list + value]
        return self.__list

    def insert(self, value, index: int):
        list_a = self.__list[0:index]
        list_a.append(value)
        list_b = self.__list[index:]
        self.__list = list_a + list_b
        return self.__list

    def pop(self):
        removed_val = self.__list.pop()
        return removed_val

    def clear(self):
        self.__list = []

    def __str__(self):
        return "[" + ", ".join(str(num) for num in self.__list) + "]"


cl = CustomList(1, 2, 3)

print(f"Printing list: {cl}")
print(f"Appending val(4): {cl.append(4)}")
print(f"Removing index[0]: {cl.remove(0)}")  # returns 1
print(f"Extending with list(5, 6): {cl.extend([5, 6])}")
print(f"Inserting 'test' at idx[3]: {cl.insert("test", 3)}")
print(f"removing last value: {cl.pop()}")
print(f"Clears list: {cl.clear()}")
print(f"Current state of list: {cl}")

