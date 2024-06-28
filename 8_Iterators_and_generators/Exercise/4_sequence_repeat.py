class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1

        if self.idx >= self.number:
            raise StopIteration

        word_index = self.idx % len(self.sequence)

        return self.sequence[word_index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print()

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

