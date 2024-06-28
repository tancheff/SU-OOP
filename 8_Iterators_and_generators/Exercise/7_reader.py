class read_next:
    def __init__(self, *args):
        self.index = - 1
        self.collection = args

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        if self.index >= len(self.collection):
            raise StopIteration

        for symbol in self.collection[self.index]:
            return symbol


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

print()

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
