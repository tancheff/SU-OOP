class vowels:
    ALL_VOWELS = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']

    def __init__(self, letters: str):
        self.letters = letters
        self.collection = list(self.letters)
        self.start_index = -1
        self.end_index = len(self.collection)

    def __iter__(self):
        return self

    def __next__(self):
        self.start_index += 1

        while self.start_index < self.end_index:
            if self.collection[self.start_index] in self.ALL_VOWELS:
                return self.collection[self.start_index]
            else:
                self.start_index += 1

        raise StopIteration()


my_string = vowels('Abcedifuty0ot')
for char in my_string:
    print(char)
