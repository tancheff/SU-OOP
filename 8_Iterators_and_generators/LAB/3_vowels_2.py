class vowels:
    ALL_VOWELS = ['a', 'e', 'i', 'o', 'u', 'y', ]

    def __init__(self, collection: str):
        self.collection = list(collection)
        self.vowels = [c for c in self.collection if c.lower() in vowels.ALL_VOWELS]
        self.current_index = -1
        self.end_index = len(self.vowels)

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index < self.end_index:
            return self.vowels[self.current_index]

        raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
