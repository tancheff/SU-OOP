class HashTable:
    def __init__(self):
        self.__max_capacity = 4
        self.__keys = [None] * self.__max_capacity
        self.__values = [None] * self.__max_capacity

    def __setitem__(self, key, value):
        index = self.__calc_index(key)

        self.__keys[index] = key
        self.__values[index] = value

    def __calc_index(self, key):
        index = sum(ord(c) for c in key) % self.__max_capacity

        index = self.__get_index(index)

        # if self.__keys[index]:
        #     pass

        return index

    def __get_index(self, index):
        while True:
            if self.__keys[index] is None:
                return index

            index += 1


table = HashTable()
table["name"] = "Peter"
table["age"] = 25

a = 5

# print(table)
# print(table.get("name"))
# print(table["age"])
# print(len(table))
